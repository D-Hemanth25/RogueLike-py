import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screenWidth = 80
    screenHeight = 50

    # we could also use // for integer division but wrapping values in int() will always guarantee an int
    playerX, playerY = int(screenWidth / 2), int(screenHeight / 2)

    tileset = tcod.tileset.load_tilesheet(
        "assets/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    eventHandler = EventHandler()

    with tcod.context.new_terminal(
        screenWidth,
        screenHeight,
        tileset=tileset,
        title="@-Adventures",
        vsync=True,
    ) as context:
        # default order is [y, x] wiht order="F" the order becomes [x, y]
        rootConsole = tcod.Console(screenWidth, screenHeight, order="F") 
        while True:
            rootConsole.print(x=playerX, y=playerY, string="@")
            context.present(rootConsole)
            rootConsole.clear()

            for event in tcod.event.wait():
                action = eventHandler.dispatch(event)

                if not action: continue

                if isinstance(action, MovementAction):
                    playerX += action.dx
                    playerY += action.dy
                
                elif isinstance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()
