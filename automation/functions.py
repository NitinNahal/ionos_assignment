class Cuboid():

    def __init__(self):
        self.edge_a = ""
        self.edge_b = ""
        self.edge_c = ""
        self.volume = ""
        self.surface_area = ""
        self.perimeter = ""

    def compute_volume(self):
        try:
            self.volume = self.edge_a * self.edge_b * self.edge_c
        except Exception as compute_volume_exception:
            print("Exception in computing Volume : " +  str(compute_volume_exception))

    def compute_surface_area(self):
        try:
            self.surface_area = 2 * ((self.edge_a * self.edge_b) + (self.edge_b * self.edge_c) + (self.edge_c*self.edge_a))
        except Exception as compute_surface_area_exception:
            print("Exception in computing SA : " +  str(compute_surface_area_exception))

    def compute_perimeter(self):
        try:
            self.perimeter = self.edge_a + self.edge_b + self.edge_c
        except Exception as compute_perimeter_exception:
            print("Exception in computing Perimeter : " +  str(compute_perimeter_exception))

    def perform_action(self):
        try:
            print("Starting .....")
            print("Please provide following inputs, assuming all values are in same units.\nSurface Area is Total Surface area")
            self.edge_a = float(input("Enter the value of edge a : "))
            self.edge_b = float(input("Enter the value of edge b : "))
            self.edge_c = float(input("Enter the value of edge c : "))

            if self.edge_a < 1 or self.edge_b < 1 or self.edge_c < 1:
                raise Exception("Value of Edge cannot be < 1")

            self.compute_volume()
            self.compute_surface_area()
            self.compute_perimeter()

        except Exception as perform_action_exception:
            print("Exception in taking input - " + str(perform_action_exception))

    def perform_action_inputs(self, edge_a, edge_b, edge_c):
        try:
            print("Starting .....")
            print("Please provide following inputs, assuming all values are in same units.\nSurface Area is Total Surface area")
            self.edge_a = float(edge_a)
            self.edge_b = float(edge_b)
            self.edge_c = float(edge_c)

            if self.edge_a < 1 or self.edge_b < 1 or self.edge_c < 1:
                raise Exception("Value of Edge cannot be < 1")

            self.compute_volume()
            self.compute_surface_area()
            self.compute_perimeter()

        except Exception as perform_action_inputs_exception:
            print("Exception in taking input - " + str(perform_action_inputs_exception))

# try:
#     new_cuboid = Cuboid()
#     new_cuboid.perform_action()
#     print("Volume - " +str(new_cuboid.volume))
#     print("Surface Area - " +  str(new_cuboid.surface_area))
#     print("Perimeter - " + str(new_cuboid.perimeter))

# except Exception as e:
#     print("Please confirm on the inputs : " + str(e))


