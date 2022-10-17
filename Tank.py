class Tank:
    model = 'Меркава'
    armor = 1000
    damage = 700
    health = 2500


    def init(self, model = str, armor = int, damage = randint(), health = int):
        self.model = model
        self.armor = armor
        self.damage = damage
        self.health = health


    def print_info(self):
        print( f'{self.model} имеет лобовую броню {self.armor} мм. при {self.health} ед. здоровья и урон в {self.damage} единиц')

    def shots(self):
        if self.damage > Tank.health:
            print (f'Экипаж танка {Tank.model} уничтожен')
        if self.damage < Tank.health:
            Tank.health = Tank.health - self.damage
            print (f'{self.model}: Точно в цель, у противника {Tank.model} осталось {Tank.health} единиц здоровья')
            self.health_down()

    def health_down(self):
        self.health = self.health - (Tank.damage/self.armor)
        print (f"{self.model}: Командир, по экипажу {self.model} попали, у нас осталось {self.health} очков здоровья")