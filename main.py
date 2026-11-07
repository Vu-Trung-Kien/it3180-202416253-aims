from aims import __version__
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


def main():
    print(f"AIMS-mini v{__version__}")
    cart = Cart()
    cart.add_digital_video_disc(
        DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95))
    cart.add_digital_video_disc(
        DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95))
    cart.add_digital_video_disc(
        DigitalVideoDisc("Aladdin", "Animation", "John Musker", 90, 18.99))
    cart.print_cart()
    print(f"Total cost: {cart.total_cost():.2f} $")


if __name__ == "__main__":
    main()
