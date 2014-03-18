from bge import logic

class gun:
    def CreateGun(self, setName, setDamage, setAuto, setFreqRate):
        self.name = setName
        self.damage = setDamage
        self.auto = setAuto
        self.freqRate = setFreqRate
        
def InitializeGuns():
    pistol = gun
    mk47 = gun
    pistol.CreateGun(gun, "Pistol", 2, False, 0)
    mk47.CreateGun(gun, "MK-47", 2, True, 15)
    print (pistol.name)
    
    
def PrintMessage():
    print ("HEY, I'M WORKING!")    
    
    