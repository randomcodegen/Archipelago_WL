from typing import TYPE_CHECKING, Dict, Set

from NetUtils import ClientStatus
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient
import time
from worlds.wl.Locations import checkable_locations
from worlds.wl.Items import lookup_trapid_to_name,lookup_eventid_to_name

powerup_list=[0xA40000,0xA40100,0xA40200,0xA40300,0xA41100]

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext
else:
    BizHawkClientContext = object


EXPECTED_ROM_NAME = "WARIOLANDAP"

class WarioLandClient(BizHawkClient):
    
    game = "Wario Land"
    system = "GB"
    patch_suffix = ".apwl"

    def __init__(self) -> None:
        super().__init__()

    async def validate_rom(self, ctx: BizHawkClientContext) -> bool:
        from CommonClient import logger
        try:
            # Check ROM name/patch version
            rom_name_bytes = ((await bizhawk.read(ctx.bizhawk_ctx, [(0x134, 16, "ROM")]))[0])
            rom_name = bytes([byte for byte in rom_name_bytes if byte != 0]).decode("ascii")
            if rom_name.startswith("SUPERMARIO"):
                logger.info("ERROR: You appear to be running an unpatched version of Wario Land. "
                            "You need to generate a patch file and use it to create a patched ROM.")
                return False
            if not rom_name.startswith(EXPECTED_ROM_NAME):
                logger.info("ERROR: The patch file used to create this ROM is not compatible with "
                            "this client. Double check your client version against the version being "
                            "used by the generator.")
                return False
        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False  # Should verify on the next pass

        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.125

        return True

    async def set_auth(self, ctx: BizHawkClientContext) -> None:
        from CommonClient import logger
        slot_name_length= await bizhawk.read(ctx.bizhawk_ctx, [(0x674B0, 1, "ROM")])
        slot_name_bytes = await bizhawk.read(ctx.bizhawk_ctx, [(0x674B1, slot_name_length[0][0], "ROM")])
        ctx.auth = bytes([byte for byte in slot_name_bytes[0] if byte != 0]).decode("utf-8")

    async def game_watcher(self, ctx: BizHawkClientContext) -> None:
        from CommonClient import logger
        connected=False
        game_clear=False

        if ctx.server_version.build > 0:
            connected=True
        else:
            connected=False
        #TODO: Catch version mismatch which throws an error

        if connected:    
            try:
                # Santity check game state, these bytes represent the first bytes of savefile1
                sanity_check_savefile = b'\x19d9W'
                read_result = await bizhawk.guarded_read(
                    ctx.bizhawk_ctx,
                    [(0xA000, 4, "System Bus")],
                    [(0xA000,sanity_check_savefile, "System Bus")])
    
                if read_result is None:  # Game not loaded
                    return

                # Check if initial sync is required
                sync_required = await bizhawk.guarded_read(
                    ctx.bizhawk_ctx,
                    [(0xA4FE, 1, "System Bus")],
                    [(0xA4FE,b'\x00', "System Bus")])
    
                if sync_required:
                    # Activate full overworld+subworld movement
                    new_value=b'\xFF'
                    for addr in range (0xA413, 0xA421):
                        await bizhawk.write(ctx.bizhawk_ctx,
                                                [(addr, new_value , "System Bus")])
                # Check Locations for completion
                new_checks=[]
                for loc_name, loc_id in checkable_locations.items():
                    if loc_id not in ctx.locations_checked:
                        loc_bitmask=(loc_id)&0xFF
                        loc_addr=(loc_id>>8)
                        read_result= await bizhawk.read(
                            ctx.bizhawk_ctx,
                            [(loc_addr, 1, "System Bus")])
                        loc_result=(read_result[0][0])&loc_bitmask
                        if loc_result>0:
                            new_checks.append(loc_id)
                
                # Number of received items stored at 0xA4FF
                read_result= await bizhawk.read(
                        ctx.bizhawk_ctx,
                        [(0xA4FF, 1, "System Bus")])
                local_received=read_result[0][0]
    
                # Grab important info for item activation timing
                read_result= await bizhawk.read(
                        ctx.bizhawk_ctx,
                        [(0xA8C3, 1, "System Bus")])
                # 0=stopped; 1=overworld; 2=level loading; 3=gameplay; 5=respawn/leave stage; 10=door transition
                game_mode=read_result[0][0]
    
                read_result= await bizhawk.read(
                        ctx.bizhawk_ctx,
                        [(0xA8C6, 1, "System Bus")])
                # demo mode needs to be 0
                demo_mode=read_result[0][0]
    
                read_result= await bizhawk.read(
                        ctx.bizhawk_ctx,
                        [(0xA908, 1, "System Bus")])
                # 0=unpaused, 1=paused
                paused=read_result[0][0]
                
    
                # Update local items if the client received new ones
                if len(ctx.items_received)>local_received:
                    for item in ctx.items_received[local_received:]:
                        # Traps
                        if item.item in lookup_trapid_to_name:
                            local_received+=1
                            if sync_required:
                                # Don't activate Traps in resync
                                pass
                            #TODO: Handle traps via queue
                            if demo_mode==0 and game_mode==3 and paused==0:
                                if item.item == 0xA38400:
                                    # Stun trap, 0xA384 = 0xFF
                                    await bizhawk.write(ctx.bizhawk_ctx,
                                                    [(0xA384, b'\xFF' , "System Bus")])
                                elif item.item == 0xA96400:
                                    # Timer trap
                                    await bizhawk.write(ctx.bizhawk_ctx,
                                                    [(0xA964, b'\x01\x01' , "System Bus")])
                                elif item.item == 0xA91A00:
                                    # Death trap
                                    await bizhawk.write(ctx.bizhawk_ctx,
                                                    [(0xA91A, b'\x09' , "System Bus")])
                                else:
                                    # Grease trap
                                    await bizhawk.write(ctx.bizhawk_ctx,
                                                    [(0xA61C, b'\x22' , "System Bus")])
                        # Everything else
                        else:
                            item_addr=item.item>>8
                            read_result= await bizhawk.read(
                                ctx.bizhawk_ctx,
                                [(item_addr, 1, "System Bus")])
                            if item.item==0xA80900 and (read_result[0][0]) & 0xF == 9:
                                if ((read_result[0][0])>>4) == 9:
                                    #if 0x99, do nothing
                                    new_value=read_result[0][0]
                                else:
                                    # Since the game directly displays hex values for lives we need to skip over A-F
                                    new_value=(read_result[0][0]+7).to_bytes(1, 'little')
                            else:
                                new_value=(read_result[0][0]+1).to_bytes(1, 'little')
                            local_received+=1
                            await bizhawk.write(ctx.bizhawk_ctx,
                                                [(item_addr, new_value , "System Bus")])
                            if item.item in powerup_list:
                                # If an upgrade item is received, make sure Wario can grow.
                                await bizhawk.write(ctx.bizhawk_ctx,
                                                [(0xA410, b'\x01' , "System Bus")])
                                if item.item == 0xA41100:
                                    # We received a progressive powerup, handle accordingly
                                    upgrade_state=read_result[0][0]+1
                                    if upgrade_state == 1:
                                        # Garlic
                                        await bizhawk.write(ctx.bizhawk_ctx,
                                                [(0xA400, b'\x01' , "System Bus")])
                                    elif upgrade_state == 2:
                                        # Bull
                                        await bizhawk.write(ctx.bizhawk_ctx,
                                                [(0xA401, b'\x01' , "System Bus")])
                                    elif upgrade_state == 3:
                                        # Dragon
                                        await bizhawk.write(ctx.bizhawk_ctx,
                                                [(0xA403, b'\x01' , "System Bus")])
                                    elif upgrade_state == 4:
                                        # Jet
                                        await bizhawk.write(ctx.bizhawk_ctx,
                                                [(0xA402, b'\x01' , "System Bus")])
                                    else:
                                        # TODO: Report that something went wrong with progressive powerups?
                                        pass
                            # Events
                            if item.item in lookup_eventid_to_name:
                                # Boss tokens
                                if item.item == 0xA41200 and read_result[0][0]+1>=ctx.slot_data['bosses_required']:
                                    # We received the required ammount of boss tokens to fight the final boss
                                    await bizhawk.write(ctx.bizhawk_ctx,
                                                [(0xA427, b'\x01' , "System Bus")])
                            # Handle garlic hunt
                            if ctx.slot_data['goal']==1 and item.item == 0xA44000 and not ctx.finished_game:
                                if read_result[0][0]+1>=ctx.slot_data['number_of_garlic_cloves'] * (ctx.slot_data['percentage_of_garlic_cloves']/ 100.0):
                                    game_clear=True
                # oof
                if len(ctx.items_received)<local_received:
                    logger.info("Desync of local received items count. Fix applied.")
                    local_received=len(ctx.items_received)
                await bizhawk.write(ctx.bizhawk_ctx,
                                                [(0xA4FF, local_received.to_bytes(1, 'little') , "System Bus")])
                
                # Update locations if we checked a new one
                for new_check_id in new_checks:
                    ctx.locations_checked.add(new_check_id)
                    location = ctx.location_names[new_check_id]
                    if not sync_required:
                        # Live checks show extra info
                        logger.info(f'New Check: {location} ({len(ctx.locations_checked)}/{len(ctx.missing_locations) + len(ctx.checked_locations)})')
                    await ctx.send_msgs([{"cmd": 'LocationChecks', "locations": [new_check_id]}])

                # Check for genie goal if required
                if ctx.slot_data['goal']==0 and not ctx.finished_game:
                    # Check for genie completion
                    read_result= await bizhawk.read(
                        ctx.bizhawk_ctx,
                        [(0xA817, 1, "System Bus")])
                    if read_result[0][0]==1:
                        game_clear=True
                
                # Resync-Loop finished
                if sync_required:
                    await bizhawk.write(ctx.bizhawk_ctx,
                                                [(0xA4FE, b'\x01' , "System Bus")])
                
                if not ctx.finished_game and game_clear:
                    await ctx.send_msgs([{
                        "cmd": "StatusUpdate",
                        "status": ClientStatus.CLIENT_GOAL
                    }])
                    ctx.finished_game=True

                # TODO: Send Tracker Data

            except bizhawk.RequestFailedError:
                # Exit handler and return to main loop to reconnect
                pass