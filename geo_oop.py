import pandas as pd


class rock:
    total = 0

    def __init__(self, lithology, age, environment):
        self.lithology = lithology
        self.environment = environment
        self.age = age
        rock.total += 1

    def convert(self):
        return {"lithology": self.lithology, "age": self.age, "environment": self.environment}


limestone = rock("limestone", "mesozoic", "lagoon")
sandstone = rock("sandstone", "lower permian", "fan delta")
blueschist = rock("blueschist", "late cretaceous", "subduction zone")

print(f"total: {rock.total}")
print(sandstone.__dict__)


rocklist = [sandstone, limestone, blueschist]

df = pd.DataFrame.from_records([i.__dict__ for i in rocklist])
print(df)


# inheritance

class geophysics(rock):
    def __init__(self, lithology, age, environment, velocity):
        super().__init__(lithology, age, environment)
        self.velocity = velocity

    def P_impedance(self, density):
        self.p_impedance = self.velocity*density


sandstone = geophysics("sandstone", "lower permian", "fan delta", 5800)
print(sandstone.__dict__)

geophysics.P_impedance(sandstone, 2.2)
print(sandstone.__dict__)

geophysics.P_impedance(sandstone, 2.5)

print(f"Sandstone P impedance is: {str(sandstone.p_impedance)}")

rocklist = [sandstone, limestone, blueschist]
df2 = pd.DataFrame.from_records([r.__dict__ for r in rocklist])
print(df2)

print("-------------")
df3 = pd.DataFrame.from_records([r.convert() for r in rocklist])
print(df3)
