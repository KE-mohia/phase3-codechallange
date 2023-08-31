class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating_value

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def all(self):
        return Review.all_reviews
