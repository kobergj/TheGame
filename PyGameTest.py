import visualization.slide as s


if __name__ == '__main__':
    slide = s.Slide()

    slide.AddButton(' --- You Are At Earth ---- ')
    slide.AddButton('[ENTER] Continue')
    slide.AddButton('[1] Get Going')

    while True:
        slide.Handle()
        slide.Draw()
