import tcod

def main() -> None:
    screenWidth = 80
    screenHeight = 50

    tileset = tcod.tileset.load_tilesheet(
        "assets/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

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
            rootConsole.print(x=1, y=1, string="@")
            context.present(rootConsole)

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()

if __name__ == "__main__":
    main()
