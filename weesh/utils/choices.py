class WeeshCategoryChoices:
    """
    Categories of Weeshs:
    ELECTRONICS : Laptops, Tvs
    FURNITURE : Chairs, Tables
    VOLUNTEER_SERVICE : Teachers
    FUNDS : Cash
    EDUCATIONAL_MATERIALS : Books
    Others:
    """

    (
        ELECTRONICS,
        FURNITURE,
        VOLUNTEER_SERVICE,
        FUNDS,
        EDUCATIONAL_MATERIALS,
        OTHERS,
    ) = range(6)
    CATEGORIES = (
        (ELECTRONICS, "ELECTRONICS"),
        (FURNITURE, "FURNITURE"),
        (VOLUNTEER_SERVICE, "VOLUNTEER_SERVICE"),
        (FUNDS, "FUNDS"),
        (EDUCATIONAL_MATERIALS, "EDUCATIONAL_MATERIALS"),
        (OTHERS, "OTHERS"),
    )


class OrganizationCategoryChoices:
    """
    Organization Category:
    Animal Charities
    Arts and Culture Charities
    Community Development Charities
    Education Charities
    Environmental Charities
    Health Charities
    Human Services
    """

    pass
