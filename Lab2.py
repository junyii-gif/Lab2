def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32")

def calc_average_temperature(num_list):
    average = sum(num_list)/ len(num_list)
    return average

def get_user_input():
    user_input = input("Number:")
    num_list = [float(x) for x in user_input.split(",")]
    return num_list

def calc_min_max_temperature(num_list):
    minimum = (min(num_list))
    maximum = (max(num_list))
    return [minimum, maximum]

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average = calc_average_temperature(num_list)
    min_max = calc_min_max_temperature(num_list)
    print(num_list)
    print(f"Average temperature = {average:.2f}")
    print(f"Min Temperature = {min_max[0]}, Max Temperature = {min_max[1]}")

if __name__ == "__main__":
    main()