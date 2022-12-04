class Robo:
    def __init__(self, my_en, my_arm, model, enemies, en_en, phi):
        self.model = model  # G – охрана; D – защита; A – атака; P – патрулирование
        self.my_en = my_en  # текущий запас энергии робота
        self.my_arm = my_arm  # текущий запас единиц вооружения
        self.enemies = enemies  # количество врагов
        self.en_en = en_en  # средний запас энергии вражеского юнита
        self.phi = phi  # угол до самой опасной вражеской цели

    def whatpower(self):  # метод определяет X единиц энергии
        if self.my_en >= 100:
            return 100
        else:
            return self.my_en

    def whatfire(self):
        return min([20, self.my_arm])

    def whatside(self):
        pass

    def fire_back(self):
        if abs(self.phi) >= 5 or self.enemies == 0:
            return 'BACKWARD'
        else:
            return 'FIRE'

    def fire_forw(self):
        if abs(self.phi) >= 10 or self.enemies == 0:
            return 'FRONT'
        else:
            return 'FIRE'

    def whattodo(self):  # возвращает команду в нужном формате
        side = self.whatside()
        if side == 'STOP':
            return side, ''
        elif side == 'FIRE':
            p = self.whatfire()
            return side, p
        else:
            x = self.whatpower()
            return side, x


class Gvard(Robo):
    def gvard_(self):
        if self.enemies == 0:
            return 'STOP'
        else:
            if abs(self.phi) < 5:
                return 'FIRE'
            elif self.phi >= 5:
                return 'LEFT'
            elif self.phi <= -5:
                return 'RIGHT'
    def whatside(self):
        return self.gvard_()


class Attak(Robo):
    def __init__(self, my_en, my_arm, model, enemies, en_en, phi):
        self.friends, self.fr_en = map(int, input().split())#количество своих роботов и средний запас энергии своих роботов
        self.model = model  # G – охрана; D – защита; A – атака; P – патрулирование
        self.my_en = my_en  # текущий запас энергии робота
        self.my_arm = my_arm  # текущий запас единиц вооружения
        self.enemies = enemies  # количество врагов
        self.en_en = en_en  # средний запас энергии вражеского юнита
        self.phi = phi  # угол до самой опасной вражеской цели

    def whatside(self):
        if self.friends * self.fr_en > self.enemies * self.en_en * 3:
            return self.fire_forw()
        else:
            return self.fire_back()


class Defend(Gvard):
    def defend_(self):
        if self.enemies * 20 >= self.my_arm:
            return self.fire_back()
        else:  # должен быть вызван whatside() изGvard
            return self.gvard_()
    def whatside(self):
        return self.defend_()


class Patrul(Defend):
    def __init__(self, my_en, my_arm, model, enemies, en_en, phi):
        self.depart = int(input())#угол отклонения от очередной точки маршрута
        self.model = model  # G – охрана; D – защита; A – атака; P – патрулирование
        self.my_en = my_en  # текущий запас энергии робота
        self.my_arm = my_arm  # текущий запас единиц вооружения
        self.enemies = enemies  # количество врагов
        self.en_en = en_en  # средний запас энергии вражеского юнита
        self.phi = phi  # угол до самой опасной вражеской цели

    def whatside(self):
        if self.enemies > 0:  # должен быть вызван whatside() Defend
            return self.defend_()
        else:
            if abs(self.depart) <= 20:
                return 'FRONT'
            elif abs(self.depart) >= 160:
                return 'BACKWARD'
            elif -91 < self.depart < -20 or 160 > self.depart > 90:
                return 'RIGHT'
            elif 91 > self.depart > 20 or -90 > self.depart > -160:
                return 'LEFT'

my_en, my_arm = map(int, input().split())
model = input()
enemies, en_en, phi = map(int, input().split())
if model == 'A':
    robot = Attak(my_en, my_arm, model, enemies, en_en, phi)
elif model == 'P':
    robot = Patrul(my_en, my_arm, model, enemies, en_en, phi)
elif model == 'G':
    robot = Gvard(my_en, my_arm, model, enemies, en_en, phi)
elif model == 'D':
    robot = Defend(my_en, my_arm, model, enemies, en_en, phi)

print(' '.join(map(str, robot.whattodo())))
