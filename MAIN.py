import tkinter
from view_MealHealthy import HealthyMealView


if __name__ == "__main__":
    root = tkinter.Tk()
    app = HealthyMealView(master=root)
    app.mainloop()
