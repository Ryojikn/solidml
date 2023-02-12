from abc import ABC, abstractmethod

################# Violates ISP #############################
# class Recommender(ABC):
#
#     @abstractmethod
#     def get_closest_items(self, item):
#         pass
#
#     @abstractmethod
#     def get_personalised_recommendations(self, user):
#         pass
#
#
# class CollaborativeFilteringRecommender(Recommender):
#
#     def get_closest_items(self, item):
#         print("Recommended closest items")
#
#     def get_personalised_recommendations(self, user):
#         print("Provided personalised recommendations")
#
#
# class DLRecommender(Recommender):
#
#     def get_closest_items(self, item):
#         print("Recommended closest items")
#
#     def get_personalised_recommendations(self, user):
#         print("Provided personalised recommendations")
#
#
# class NearestNeighbourRecommender(Recommender):
#
#     def get_closest_items(self, item):
#         print("Recommended closest items")
#
#     def get_personalised_recommendations(self, user):
#         raise Exception("NearestNeighbourRecommender can't provide personalised recommendations")
################# Violates ISP #############################


# class Recommender(ABC):
#
#     @abstractmethod
#     def get_closest_items(self, item):
#         pass
#
#
# class PersonalisedRecommender(Recommender):
#
#     @abstractmethod
#     def get_personalised_recommendations(self, user):
#         pass
#
#
# class CollaborativeFilteringRecommender(PersonalisedRecommender):
#
#     def get_closest_items(self, item):
#         print("Recommended closest items")
#
#     def get_personalised_recommendations(self, user):
#         print("Provided personalised recommendations")
#
#
# class DLRecommender(PersonalisedRecommender):
#
#     def get_closest_items(self, item):
#         print("Recommended closest items")
#
#     def get_personalised_recommendations(self, user):
#         print("Provided personalised recommendations")
#
#
# class NearestNeighbourRecommender(Recommender):
#
#     def get_closest_items(self, item):
#        print("Recommended closest items")


class ItemRecommender(ABC):
    @abstractmethod
    def get_closest_items(self, item):
        pass


class PersonalisedRecommender(ABC):
    @abstractmethod
    def get_personalised_recommendations(self, user):
        pass


class CollaborativeFilteringRecommender(ItemRecommender, PersonalisedRecommender):
    def get_closest_items(self, item):
        print("Recommended closest items from CollaborativeFilteringRecommender")

    def get_personalised_recommendations(self, user):
        print(
            "Provided personalised recommendations from CollaborativeFilteringRecommender"
        )


class DLRecommender(ItemRecommender, PersonalisedRecommender):
    def get_closest_items(self, item):
        print("Recommended closest items from DLRecommender")

    def get_personalised_recommendations(self, user):
        print("Provided personalised recommendations from DLRecommender")


class NearestNeighbourRecommender(ItemRecommender):
    def get_closest_items(self, item):
        print("Recommended closest items from NearesNeighbourRecommender")


if __name__ == "__main__":
    recommender = CollaborativeFilteringRecommender()
    recommender.get_closest_items(item=1)
    recommender.get_personalised_recommendations(user=1)
    recommender = DLRecommender()
    recommender.get_closest_items(item=1)
    recommender.get_personalised_recommendations(user=1)
    recommender = NearestNeighbourRecommender()
    recommender.get_closest_items(item=1)
