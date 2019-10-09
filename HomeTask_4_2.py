import random;
class Warrior:
    name="";
    health=random.randint(100,150);
    attack_power=random.randint(20,30);
    def __init__(self, name):
        self.name=name;
    def Health(self):
        return self.health;
    def Power(self):
        return self.attack_power;
    def Damage(self, newPower1):
        self.health=self.health-newPower1;
        if self.health<0:
            return self.name+" "+"получил "+str(newPower1)+" урона и погиб";
        else:
            return self.name+" "+"получил "+str(newPower1)+" урона. Осталось " + str(self.health)+" "+"здоровья";
class Shield_Warrior(Warrior):

    def Damage(self, newPower1):
        protection = random.randint(5, 10);
        self.health = self.health - newPower1+protection;
        r = newPower1 - protection
        if self.health < 0:
            return self.name + " " + "получил " + str(r) + " урона и погиб";
        else:
            return self.name + " " + "получил " + str(r) + " урона. Осталось " + str(self.health) + " " + "здоровья";
class Expert_Warrior(Warrior):

    def Power(self):
        newPower = self.attack_power;
        x = random.random()
        if x <= 0.2:
            return 2*newPower;
        else:
            return newPower;

#bers = Warrior("Берсерк");
#print(bers.name);
#print(bers.attack_power);
#shield = Shield_Warrior("Защитник");
#print(shield.name);
#print(shield.Power());
#expert = Expert_Warrior("Эксперт");
#print(expert.name);
#print(expert.Power());
def Play():
    pl1=Warrior("Воин1");
    pl2=Shield_Warrior("Воин2");
    print(pl1.name, "здоровье: ", pl1.health);
    print(pl2.name,"здоровье: ", pl2.health);
    print(pl1.name, "максимальная сила атаки: ", pl1.attack_power);
    print(pl2.name, "максимальная сила атаки: ", pl2.attack_power);
    print("Воин1 наносит удар");
    print(pl2.Damage(pl1.Power()));
    while True:
        print("Воин2 наносит удар");
        print(pl1.Damage(pl2.Power()));
        if pl1.Health() <= 0 and pl2.Health() > 0:
            print("Победил Воин2");
            return False;
        elif pl2.Health() <=0 and pl1.Health() > 0:
            print("Победил Воин1");
            return False;
        elif pl2.Health() == 0 and pl1.Health() == 0:
            print("Ничья")
            return False;
        else:
            print("Воин1 наносит удар")
            print(pl2.Damage(pl1.Power()))

print(Play())





