from class_homeapplience import HomeAppliance


class Blender(HomeAppliance):
    def blend(self) -> None:
        if self.is_on:
            print("Blending at speed", self.speed)
        else:
            print("Blender is off. Please turn it on first.")
