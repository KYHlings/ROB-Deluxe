    if match == 3:
        print("hej match 4")
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_green_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)
            print(len(player1.images))
            print(player1.frame)


    if match == 3:
        print("hej match 4")
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_purple_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)
            print(len(player1.images))
            print(player1.frame)