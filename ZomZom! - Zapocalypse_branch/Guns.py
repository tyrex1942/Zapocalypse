from bge import logic

class gun:
    def CreateGun(self, setName, setDamage, setAuto, setFreqRate):
        self.name = setName
        self.damage = setDamage
        self.auto = setAuto
        self.freqRate = setFreqRate
        
def InitializeGuns():
    pistol = gun
    pistol.CreateGun(gun, "Pistol", 2, False, 0)
    