from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class QqHuxuanResource(BaseResource):
    """Generated resource for QQ Huxuan Creator Marketplace."""

    def cgi_bin_advertiser_finder_publisher_search_v1(
        self,
        *,
        keyword: str | None = "",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Video Account Creator Search

        Searches or browses QQ Huxuan Video Account creators by optional nickname keyword with page-number pagination. Use it to discover and shortlist video creators for Tencent Huxuan campaign planning.

        Args:
            keyword: Creator nickname keyword. Leave empty to browse the default marketplace list.
            page: Page number. The first page is 1.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/finder_publisher/search/v1",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def cgi_bin_advertiser_mp_publisher_search_v1(
        self,
        *,
        keyword: str | None = "",
        page: int | None = 1,
        creator_types: list[Any] | None = None,
        fans_levels: list[Any] | None = None,
    ) -> ApiResponse[Any]:
        """
        Official Account Creator Search

        Searches QQ Huxuan Official Account creators by keyword, creator categories and eight preset follower-count ranges, with multiple selections and page-number pagination. Use it to shortlist publishers for campaign planning.

        Args:
            keyword: Creator nickname or account keyword. Leave empty to browse the default marketplace list.
            page: Page number. The first page is 1.
            creator_types: Comma-separated creator categories or subcategories. A top-level category includes all its subcategories. Multiple selections are combined; leave unset for all categories.  Available Values: - `SOCIETY`: Society (all subcategories) - `SOCIETY_ACCIDENTS_AND_DISASTERS`: Society: Accidents and disasters - `SOCIETY_PUBLIC_INTEREST`: Society: Public interest - `SOCIETY_ODDITIES_AND_CURIOSITIES`: Society: Oddities and curiosities - `SOCIETY_POSITIVE_STORIES`: Society: Positive stories - `SOCIETY_LEGAL_DISPUTES`: Society: Legal disputes - `SOCIETY_LAWS_AND_REGULATIONS`: Society: Laws and regulations - `SOCIETY_OVERSEAS_LIVELIHOODS`: Society: Overseas livelihoods - `SOCIETY_COMMUNITY_NEWS`: Society: Community news - `SOCIETY_INTERNAL_ORGANIZATION_MANAGEMENT`: Society: Internal organization management - `SOCIETY_OTHER`: Society: Other - `LIFESTYLE`: Lifestyle (all subcategories) - `LIFESTYLE_COLLECTING`: Lifestyle: Collecting - `LIFESTYLE_HOUSEHOLD_GOODS`: Lifestyle: Household goods - `LIFESTYLE_DAILY_CARDS`: Lifestyle: Daily cards - `LIFESTYLE_WAYS_OF_LIVING`: Lifestyle: Ways of living - `LIFESTYLE_EVERYDAY_KNOWLEDGE`: Lifestyle: Everyday knowledge - `LIFESTYLE_LIFE_JOURNALS`: Lifestyle: Life journals - `LIFESTYLE_SHOPPING_INFORMATION`: Lifestyle: Shopping information - `LIFESTYLE_CIGARETTES`: Lifestyle: Cigarettes - `LIFESTYLE_OTHER`: Lifestyle: Other - `FASHION`: Fashion (all subcategories) - `FASHION_FASHION_EDITORIALS`: Fashion: Fashion editorials - `FASHION_FASHION_PRODUCTS`: Fashion: Fashion products - `FASHION_FASHION_EVENTS`: Fashion: Fashion events - `FASHION_FASHION_NEWS`: Fashion: Fashion news - `FASHION_MENS_FASHION`: Fashion: Men's fashion - `FASHION_OUTFIT_STYLING`: Fashion: Outfit styling - `FASHION_BODY_SHAPING_AND_COSMETIC_SURGERY`: Fashion: Body shaping and cosmetic surgery - `FASHION_HAIRSTYLING`: Fashion: Hairstyling - `FASHION_BEAUTY_AND_MAKEUP`: Fashion: Beauty and makeup - `FASHION_ACCESSORIES`: Fashion: Accessories - `FASHION_SHOES`: Fashion: Shoes - `FASHION_OTHER`: Fashion: Other - `PARENTING`: Parenting (all subcategories) - `PARENTING_POSTPARTUM`: Parenting: Postpartum - `PARENTING_PARENT_CHILD_DEVELOPMENT`: Parenting: Parent-child development - `PARENTING_PRECONCEPTION`: Parenting: Preconception - `PARENTING_PREGNANCY_AND_CHILDBIRTH`: Parenting: Pregnancy and childbirth - `PARENTING_CARE_AND_DEVELOPMENT`: Parenting: Care and development - `PARENTING_MATERNITY_AND_BABY_PRODUCTS`: Parenting: Maternity and baby products - `PARENTING_DISEASE_PREVENTION_AND_TREATMENT`: Parenting: Disease prevention and treatment - `PARENTING_BABY_PHOTOS`: Parenting: Baby photos - `PARENTING_NUTRITION`: Parenting: Nutrition - `PARENTING_OTHER`: Parenting: Other - `ADVERTISING_CREATIVITY`: Advertising creativity (all subcategories) - `ADVERTISING_CREATIVITY_PUBLIC_SERVICE_ADVERTISING`: Advertising creativity: Public service advertising - `ADVERTISING_CREATIVITY_CREATIVE_DESIGN`: Advertising creativity: Creative design - `ADVERTISING_CREATIVITY_BRAND_ADVERTISING`: Advertising creativity: Brand advertising - `ADVERTISING_CREATIVITY_PROMOTIONAL_SHORT_FILMS`: Advertising creativity: Promotional short films - `ADVERTISING_CREATIVITY_OTHER`: Advertising creativity: Other - `MUSIC`: Music (all subcategories) - `MUSIC_DJ`: Music: DJ - `MUSIC_MUSICAL_INSTRUMENTS`: Music: Musical instruments - `MUSIC_CHILDRENS_SONGS`: Music: Children's songs - `MUSIC_FILM_AND_TELEVISION_MUSIC`: Music: Film and television music - `MUSIC_LOVE_SONGS`: Music: Love songs - `MUSIC_LIVE_MUSIC`: Music: Live music - `MUSIC_CLASSICS`: Music: Classics - `MUSIC_OTHER`: Music: Other - `FINANCE`: Finance (all subcategories) - `FINANCE_INTERNET_FINANCE`: Finance: Internet finance - `FINANCE_INSURANCE`: Finance: Insurance - `FINANCE_TRUSTS`: Finance: Trusts - `FINANCE_BONDS`: Finance: Bonds - `FINANCE_FUNDS`: Finance: Funds - `FINANCE_FOREIGN_EXCHANGE`: Finance: Foreign exchange - `FINANCE_MACROECONOMICS`: Finance: Macroeconomics - `FINANCE_INVESTMENT`: Finance: Investment - `FINANCE_DIGITAL_CURRENCIES`: Finance: Digital currencies - `FINANCE_FUTURES`: Finance: Futures - `FINANCE_FINANCIAL_PLANNING_AND_INVESTMENT_TIPS`: Finance: Financial planning and investment tips - `FINANCE_STOCKS`: Finance: Stocks - `FINANCE_ENERGY`: Finance: Energy - `FINANCE_FINANCE_PERSONALITIES`: Finance: Finance personalities - `FINANCE_FINANCIAL_NEWS`: Finance: Financial news - `FINANCE_PRECIOUS_METALS`: Finance: Precious metals - `FINANCE_BANKING`: Finance: Banking - `FINANCE_OTHER`: Finance: Other - `CAREER`: Career (all subcategories) - `CAREER_ENTREPRENEURSHIP_GUIDANCE`: Career: Entrepreneurship guidance - `CAREER_BUSINESS_MANAGEMENT`: Career: Business management - `CAREER_JOB_SEARCH_AND_INTERVIEWS`: Career: Job search and interviews - `CAREER_WORKPLACE_EXPERIENCE`: Career: Workplace experience - `CAREER_OTHER`: Career: Other - `FOOD`: Food (all subcategories) - `FOOD_RESTAURANT_GUIDES`: Food: Restaurant guides - `FOOD_FOOD_CULTURE`: Food: Food culture - `FOOD_UNUSUAL_FOOD`: Food: Unusual food - `FOOD_FOOD_SNAPSHOTS`: Food: Food snapshots - `FOOD_TEA`: Food: Tea - `FOOD_RECIPES`: Food: Recipes - `FOOD_ALCOHOLIC_DRINKS`: Food: Alcoholic drinks - `FOOD_OTHER`: Food: Other - `BEAUTIFUL_WOMEN`: Beautiful women (all subcategories) - `BEAUTIFUL_WOMEN_PORTRAITS`: Beautiful women: Portraits - `BEAUTIFUL_WOMEN_STREET_PHOTOGRAPHY`: Beautiful women: Street photography - `BEAUTIFUL_WOMEN_OTHER`: Beautiful women: Other - `INFLUENCERS`: Influencers (all subcategories) - `INFLUENCERS_TALENTS_AND_SKILLS`: Influencers: Talents and skills - `INFLUENCERS_INFLUENCER_NEWS`: Influencers: Influencer news - `VARIETY_SHOWS`: Variety shows (all subcategories) - `VARIETY_SHOWS_MAINLAND_CHINESE_SHOWS`: Variety shows: Mainland Chinese shows - `VARIETY_SHOWS_JAPANESE_SHOWS`: Variety shows: Japanese shows - `VARIETY_SHOWS_GALAS_AND_CEREMONIES`: Variety shows: Galas and ceremonies - `VARIETY_SHOWS_WESTERN_SHOWS`: Variety shows: Western shows - `VARIETY_SHOWS_HONG_KONG_AND_TAIWAN_SHOWS`: Variety shows: Hong Kong and Taiwan shows - `VARIETY_SHOWS_RELATED_CONTENT`: Variety shows: Related content - `VARIETY_SHOWS_KOREAN_SHOWS`: Variety shows: Korean shows - `DOCUMENTARIES`: Documentaries (all subcategories) - `DOCUMENTARIES_PATRIOTIC_DOCUMENTARIES`: Documentaries: Patriotic documentaries - `DOCUMENTARIES_BIOGRAPHICAL_DOCUMENTARIES`: Documentaries: Biographical documentaries - `DOCUMENTARIES_MILITARY_DOCUMENTARIES`: Documentaries: Military documentaries - `DOCUMENTARIES_HISTORY_DOCUMENTARIES`: Documentaries: History documentaries - `DOCUMENTARIES_INDUSTRY_DOCUMENTARIES`: Documentaries: Industry documentaries - `DOCUMENTARIES_CULTURE_DOCUMENTARIES`: Documentaries: Culture documentaries - `DOCUMENTARIES_SOCIAL_ISSUES_DOCUMENTARIES`: Documentaries: Social issues documentaries - `DOCUMENTARIES_SCIENCE_DOCUMENTARIES`: Documentaries: Science documentaries - `DOCUMENTARIES_FOOD_DOCUMENTARIES`: Documentaries: Food documentaries - `DOCUMENTARIES_NATURE_DOCUMENTARIES`: Documentaries: Nature documentaries - `DOCUMENTARIES_OTHER`: Documentaries: Other - `TECHNOLOGY`: Technology (all subcategories) - `TECHNOLOGY_INTERNET_PLUS`: Technology: Internet Plus - `TECHNOLOGY_INFORMATION_TECHNOLOGY`: Technology: Information technology - `TECHNOLOGY_CONTENT_INDUSTRY`: Technology: Content industry - `TECHNOLOGY_EMERGING_INDUSTRIES`: Technology: Emerging industries - `TECHNOLOGY_BLOCKCHAIN`: Technology: Blockchain - `TECHNOLOGY_DIGITAL_DEVICES`: Technology: Digital devices - `TECHNOLOGY_MACHINERY`: Technology: Machinery - `TECHNOLOGY_ECOMMERCE`: Technology: E-commerce - `TECHNOLOGY_TECHNOLOGY_PERSONALITIES`: Technology: Technology personalities - `TECHNOLOGY_TECHNOLOGY_COMPANIES`: Technology: Technology companies - `TECHNOLOGY_TECHNOLOGY_VENTURE_INVESTMENT`: Technology: Technology venture investment - `TECHNOLOGY_TECHNOLOGY_CURIOSITIES`: Technology: Technology curiosities - `TECHNOLOGY_AEROSPACE`: Technology: Aerospace - `TECHNOLOGY_SOFTWARE_TOOLS`: Technology: Software tools - `TECHNOLOGY_TELECOMMUNICATIONS`: Technology: Telecommunications - `TECHNOLOGY_OTHER`: Technology: Other - `SCIENCE`: Science (all subcategories) - `SCIENCE_ANIMALS_AND_PLANTS`: Science: Animals and plants - `SCIENCE_MEDICINE`: Science: Medicine - `SCIENCE_GEOGRAPHY`: Science: Geography - `SCIENCE_ASTRONOMY_AND_SPACE`: Science: Astronomy and space - `SCIENCE_CURIOSITIES`: Science: Curiosities - `SCIENCE_BIOLOGY_AND_ARCHAEOLOGY`: Science: Biology and archaeology - `SCIENCE_SCIENTISTS`: Science: Scientists - `SCIENCE_POPULAR_SCIENCE`: Science: Popular science - `SCIENCE_SCIENTIFIC_RESEARCH`: Science: Scientific research - `SCIENCE_OTHER`: Science: Other - `TELEVISION_DRAMA`: Television drama (all subcategories) - `TELEVISION_DRAMA_RELATED_CONTENT`: Television drama: Related content - `TELEVISION_DRAMA_DRAMA_COMMENTARY`: Television drama: Drama commentary - `TELEVISION_DRAMA_HIGHLIGHT_CLIPS`: Television drama: Highlight clips - `TELEVISION_DRAMA_TRAILERS_AND_NEWS`: Television drama: Trailers and news - `FILM`: Film (all subcategories) - `FILM_SHORT_FILMS`: Film: Short films - `FILM_RELATED_CONTENT`: Film: Related content - `FILM_FILM_CLIPS`: Film: Film clips - `FILM_FILM_COMMENTARY`: Film: Film commentary - `FILM_FILM_NEWS`: Film: Film news - `FILM_TRAILERS_AND_BEHIND_THE_SCENES`: Film: Trailers and behind the scenes - `GAMING`: Gaming (all subcategories) - `GAMING_CONSOLE_GAMES`: Gaming: Console games - `GAMING_MINIGAMES`: Gaming: Minigames - `GAMING_MOBILE_GAMES`: Gaming: Mobile games - `GAMING_GAMING_NEWS`: Gaming: Gaming news - `GAMING_ESPORTS_EVENTS`: Gaming: Esports events - `GAMING_PC_GAMES`: Gaming: PC games - `GAMING_ARCADE_GAMES`: Gaming: Arcade games - `GAMING_BROWSER_GAMES`: Gaming: Browser games - `GAMING_OTHER`: Gaming: Other - `AUTOMOTIVE`: Automotive (all subcategories) - `AUTOMOTIVE_USED_CARS`: Automotive: Used cars - `AUTOMOTIVE_DRIVING_TIPS`: Automotive: Driving tips - `AUTOMOTIVE_NEW_CAR_NEWS`: Automotive: New car news - `AUTOMOTIVE_AUTOMOTIVE_INDUSTRY`: Automotive: Automotive industry - `AUTOMOTIVE_CAR_ADVERTISING`: Automotive: Car advertising - `AUTOMOTIVE_CAR_MODIFICATIONS`: Automotive: Car modifications - `AUTOMOTIVE_MODEL_CARS`: Automotive: Model cars - `AUTOMOTIVE_AUTOMOTIVE_TECHNOLOGY`: Automotive: Automotive technology - `AUTOMOTIVE_CAR_REVIEWS`: Automotive: Car reviews - `AUTOMOTIVE_CAR_CURIOSITIES`: Automotive: Car curiosities - `AUTOMOTIVE_CAR_CARE_AND_MAINTENANCE`: Automotive: Car care and maintenance - `AUTOMOTIVE_AUTO_SHOW_NEWS`: Automotive: Auto show news - `AUTOMOTIVE_OTHER`: Automotive: Other - `PUBLIC_LIFE`: Public life (all subcategories) - `PUBLIC_LIFE_TRANSPORT`: Public life: Transport - `PUBLIC_LIFE_WEATHER`: Public life: Weather - `PUBLIC_LIFE_EDUCATION_NEWS`: Public life: Education news - `PUBLIC_LIFE_LIVELIHOOD_NEWS`: Public life: Livelihood news - `PUBLIC_LIFE_PUBLIC_SECURITY`: Public life: Public security - `PUBLIC_LIFE_SOCIAL_SECURITY`: Public life: Social security - `TRADITIONAL_PERFORMING_ARTS`: Traditional performing arts (all subcategories) - `TRADITIONAL_PERFORMING_ARTS_PEKING_OPERA`: Traditional performing arts: Peking opera - `TRADITIONAL_PERFORMING_ARTS_COMEDY_SKETCHES`: Traditional performing arts: Comedy sketches - `TRADITIONAL_PERFORMING_ARTS_KUNQU_OPERA`: Traditional performing arts: Kunqu opera - `TRADITIONAL_PERFORMING_ARTS_TEOCHEW_OPERA`: Traditional performing arts: Teochew opera - `TRADITIONAL_PERFORMING_ARTS_CROSSTALK`: Traditional performing arts: Crosstalk - `TRADITIONAL_PERFORMING_ARTS_QINQIANG_OPERA`: Traditional performing arts: Qinqiang opera - `TRADITIONAL_PERFORMING_ARTS_CANTONESE_OPERA`: Traditional performing arts: Cantonese opera - `TRADITIONAL_PERFORMING_ARTS_STORYTELLING`: Traditional performing arts: Storytelling - `TRADITIONAL_PERFORMING_ARTS_HENAN_OPERA`: Traditional performing arts: Henan opera - `TRADITIONAL_PERFORMING_ARTS_YUE_OPERA`: Traditional performing arts: Yue opera - `TRADITIONAL_PERFORMING_ARTS_HUANGMEI_OPERA`: Traditional performing arts: Huangmei opera - `TRADITIONAL_PERFORMING_ARTS_OTHER`: Traditional performing arts: Other - `ASTROLOGY_AND_DIVINATION`: Astrology and divination (all subcategories) - `ASTROLOGY_AND_DIVINATION_DESTINY_READING`: Astrology and divination: Destiny reading - `ASTROLOGY_AND_DIVINATION_TAROT`: Astrology and divination: Tarot - `ASTROLOGY_AND_DIVINATION_ZODIAC_SIGNS`: Astrology and divination: Zodiac signs - `ASTROLOGY_AND_DIVINATION_PERSONALITY_TESTS`: Astrology and divination: Personality tests - `ASTROLOGY_AND_DIVINATION_CHINESE_ZODIAC`: Astrology and divination: Chinese zodiac - `ASTROLOGY_AND_DIVINATION_PHYSIOGNOMY`: Astrology and divination: Physiognomy - `ASTROLOGY_AND_DIVINATION_BLOOD_TYPES`: Astrology and divination: Blood types - `ASTROLOGY_AND_DIVINATION_FENG_SHUI`: Astrology and divination: Feng shui - `ASTROLOGY_AND_DIVINATION_OTHER`: Astrology and divination: Other - `CURRENT_AFFAIRS`: Current affairs (all subcategories) - `CURRENT_AFFAIRS_CHINESE_DIPLOMACY`: Current affairs: Chinese diplomacy - `CURRENT_AFFAIRS_DOMESTIC_NEWS`: Current affairs: Domestic news - `CURRENT_AFFAIRS_INTERNATIONAL_NEWS`: Current affairs: International news - `CURRENT_AFFAIRS_HONG_KONG_MACAU_AND_TAIWAN`: Current affairs: Hong Kong, Macau and Taiwan - `CURRENT_AFFAIRS_OTHER`: Current affairs: Other - `TRAVEL`: Travel (all subcategories) - `TRAVEL_ASIA`: Travel: Asia - `TRAVEL_NORTH_AMERICA`: Travel: North America - `TRAVEL_ANTARCTICA`: Travel: Antarctica - `TRAVEL_SOUTH_AMERICA`: Travel: South America - `TRAVEL_DOMESTIC_TRAVEL`: Travel: Domestic travel - `TRAVEL_OCEANIA`: Travel: Oceania - `TRAVEL_TOURISM_INDUSTRY`: Travel: Tourism industry - `TRAVEL_TRAVEL_ROUNDUPS`: Travel: Travel roundups - `TRAVEL_EUROPE`: Travel: Europe - `TRAVEL_AFRICA`: Travel: Africa - `TRAVEL_OTHER`: Travel: Other - `CULTURE`: Culture (all subcategories) - `CULTURE_CALLIGRAPHY`: Culture: Calligraphy - `CULTURE_PHILOSOPHY`: Culture: Philosophy - `CULTURE_CHINESE_CLASSICAL_STUDIES`: Culture: Chinese classical studies - `CULTURE_RELIGION`: Culture: Religion - `CULTURE_CRAFTS`: Culture: Crafts - `CULTURE_ARCHITECTURE`: Culture: Architecture - `CULTURE_THEATRE`: Culture: Theatre - `CULTURE_LITERATURE`: Culture: Literature - `CULTURE_CULTURAL_RELICS`: Culture: Cultural relics - `CULTURE_FOLK_CUSTOMS`: Culture: Folk customs - `CULTURE_PAINTING`: Culture: Painting - `CULTURE_GENERAL_CULTURE`: Culture: General culture - `CULTURE_DANCE`: Culture: Dance - `CULTURE_READING`: Culture: Reading - `CULTURE_SCULPTURE`: Culture: Sculpture - `CULTURE_MUSIC`: Culture: Music - `CULTURE_OTHER`: Culture: Other - `EDUCATION`: Education (all subcategories) - `EDUCATION_ACCOUNTANT_EXAMS`: Education: Accountant exams - `EDUCATION_CIVIL_SERVICE_EXAMS`: Education: Civil service exams - `EDUCATION_JUNIOR_SECONDARY_EDUCATION`: Education: Junior secondary education - `EDUCATION_HEALTHCARE_EXAMS`: Education: Healthcare exams - `EDUCATION_UNIVERSITY_EDUCATION`: Education: University education - `EDUCATION_PRESCHOOL_EDUCATION`: Education: Preschool education - `EDUCATION_PRIMARY_EDUCATION`: Education: Primary education - `EDUCATION_CONSTRUCTION_MANAGER_EXAMS`: Education: Construction manager certification exams - `EDUCATION_ADULT_EDUCATION`: Education: Adult education - `EDUCATION_VOCATIONAL_SKILLS_EDUCATION`: Education: Vocational skills education - `EDUCATION_TEACHER_EXAMS`: Education: Teacher exams - `EDUCATION_PUBLIC_SPEAKING`: Education: Public speaking - `EDUCATION_STUDY_ABROAD`: Education: Study abroad - `EDUCATION_POSTGRADUATE_EDUCATION`: Education: Postgraduate education - `EDUCATION_LANGUAGE_LEARNING`: Education: Language learning - `EDUCATION_SENIOR_SECONDARY_EDUCATION`: Education: Senior secondary education - `EDUCATION_OTHER`: Education: Other - `PHOTOGRAPHY`: Photography (all subcategories) - `PHOTOGRAPHY_POST_PROCESSING`: Photography: Post-processing - `PHOTOGRAPHY_PHOTOGRAPHIC_WORKS`: Photography: Photographic works - `PHOTOGRAPHY_PHOTOGRAPHY_EQUIPMENT`: Photography: Photography equipment - `PHOTOGRAPHY_PHOTOGRAPHY_TECHNIQUES`: Photography: Photography techniques - `PHOTOGRAPHY_OTHER`: Photography: Other - `COMEDY`: Comedy (all subcategories) - `COMEDY_VISUAL_JOKES`: Comedy: Visual jokes with hidden meanings - `COMEDY_COMEDY_FILM_AND_TELEVISION`: Comedy: Comedy film and television - `COMEDY_PRANKS`: Comedy: Pranks - `COMEDY_JOKES`: Comedy: Jokes - `COMEDY_MISCHIEVOUS_CHILDREN`: Comedy: Mischievous children - `COMEDY_FUNNY_ANIMALS`: Comedy: Funny animals - `COMEDY_WITTY_REPLIES`: Comedy: Witty replies - `COMEDY_FUNNY_COMICS`: Comedy: Funny comics - `COMEDY_OTHER`: Comedy: Other - `REAL_ESTATE`: Real estate (all subcategories) - `REAL_ESTATE_PROPERTY_TRANSACTIONS`: Real estate: Property transactions - `REAL_ESTATE_PROPERTY_POLICY`: Real estate: Property policy - `REAL_ESTATE_PROPERTY_PRICE_TRENDS`: Real estate: Property price trends - `REAL_ESTATE_OVERSEAS_PROPERTY`: Real estate: Overseas property - `REAL_ESTATE_RENTING`: Real estate: Renting - `REAL_ESTATE_OTHER`: Real estate: Other - `RELATIONSHIPS`: Relationships (all subcategories) - `RELATIONSHIPS_ROMANTIC_RELATIONSHIPS`: Relationships: Romantic relationships - `RELATIONSHIPS_INTERPERSONAL_RELATIONSHIPS`: Relationships: Interpersonal relationships - `RELATIONSHIPS_FAMILY_RELATIONSHIPS`: Relationships: Family relationships - `RELATIONSHIPS_OTHER`: Relationships: Other - `INSPIRATIONAL_WRITING`: Inspirational writing (all subcategories) - `INSPIRATIONAL_WRITING_FAMOUS_QUOTES`: Inspirational writing: Famous quotes - `INSPIRATIONAL_WRITING_CAPTIONS_AND_QUOTES`: Inspirational writing: Captions and quotes - `INSPIRATIONAL_WRITING_ESSAYS_AND_REFLECTIONS`: Inspirational writing: Essays and reflections - `HANDSOME_MEN`: Handsome men (all subcategories) - `HANDSOME_MEN_PORTRAITS`: Handsome men: Portraits - `HANDSOME_MEN_OTHER`: Handsome men: Other - `FICTION`: Fiction (all subcategories) - `FICTION_FICTION_FOR_WOMEN`: Fiction: Fiction for women - `FICTION_FICTION_FOR_MEN`: Fiction: Fiction for men - `FICTION_OTHER`: Fiction: Other - `PETS`: Pets (all subcategories) - `PETS_DOGS`: Pets: Dogs - `PETS_CATS`: Pets: Cats - `PETS_BIRDS`: Pets: Birds - `PETS_CHINCHILLAS_AND_HAMSTERS`: Pets: Chinchillas and hamsters - `PETS_OTHER`: Pets: Other - `ENTERTAINMENT`: Entertainment (all subcategories) - `ENTERTAINMENT_CELEBRITY_GOSSIP`: Entertainment: Celebrity gossip - `ENTERTAINMENT_CELEBRITIES_FROM_OTHER_REGIONS`: Entertainment: Celebrities from other regions - `ENTERTAINMENT_MAINLAND_CHINESE_CELEBRITIES`: Entertainment: Mainland Chinese celebrities - `ENTERTAINMENT_JAPANESE_CELEBRITIES`: Entertainment: Japanese celebrities - `ENTERTAINMENT_WESTERN_CELEBRITIES`: Entertainment: Western celebrities - `ENTERTAINMENT_HONG_KONG_AND_TAIWAN_CELEBRITIES`: Entertainment: Hong Kong and Taiwan celebrities - `ENTERTAINMENT_KOREAN_CELEBRITIES`: Entertainment: Korean celebrities - `ENTERTAINMENT_OTHER`: Entertainment: Other - `WALLPAPERS_AND_AVATARS`: Wallpapers and avatars (all subcategories) - `WALLPAPERS_AND_AVATARS_WALLPAPERS`: Wallpapers and avatars: Wallpapers - `WALLPAPERS_AND_AVATARS_AVATARS`: Wallpapers and avatars: Avatars - `WALLPAPERS_AND_AVATARS_TEXT_IMAGES`: Wallpapers and avatars: Text images - `WALLPAPERS_AND_AVATARS_MEMES`: Wallpapers and avatars: Memes - `WALLPAPERS_AND_AVATARS_OTHER`: Wallpapers and avatars: Other - `HISTORY`: History (all subcategories) - `HISTORY_WORLD_HISTORY`: History: World history - `HISTORY_ANCIENT_CHINESE_HISTORY`: History: Ancient Chinese history - `HISTORY_CONTEMPORARY_CHINESE_HISTORY`: History: Contemporary Chinese history - `HISTORY_MODERN_CHINESE_HISTORY`: History: Modern Chinese history - `HISTORY_CHINESE_COMMUNIST_PARTY_HISTORY`: History: Chinese Communist Party history - `HISTORY_HISTORY_AND_ARCHAEOLOGY`: History: History and archaeology - `HISTORY_UNOFFICIAL_HISTORY`: History: Unofficial history - `HISTORY_OTHER`: History: Other - `ANIMATION_AND_COMICS`: Animation and comics (all subcategories) - `ANIMATION_AND_COMICS_COSPLAY`: Animation and comics: Cosplay - `ANIMATION_AND_COMICS_ANIMATION_AND_COMICS_NEWS`: Animation and comics: Animation and comics news - `ANIMATION_AND_COMICS_ORIGINAL_SHORT_FILMS`: Animation and comics: Original short films - `ANIMATION_AND_COMICS_CHINESE_ANIMATION`: Animation and comics: Chinese animation - `ANIMATION_AND_COMICS_CHILDRENS_ANIMATION`: Animation and comics: Children's animation - `ANIMATION_AND_COMICS_ADULT_ANIMATION`: Animation and comics: Adult animation - `ANIMATION_AND_COMICS_FIGURINES`: Animation and comics: Figurines - `ANIMATION_AND_COMICS_HAND_DRAWING`: Animation and comics: Hand drawing - `ANIMATION_AND_COMICS_JAPANESE_ANIMATION`: Animation and comics: Japanese animation - `ANIMATION_AND_COMICS_WESTERN_ANIMATION`: Animation and comics: Western animation - `ANIMATION_AND_COMICS_KOREAN_ANIMATION`: Animation and comics: Korean animation - `ANIMATION_AND_COMICS_OTHER`: Animation and comics: Other - `MILITARY`: Military (all subcategories) - `MILITARY_MILITARY_COLUMNS`: Military: Military columns - `MILITARY_MILITARY_AFFAIRS`: Military: Military affairs - `MILITARY_MILITARY_HISTORY`: Military: Military history - `MILITARY_MILITARY_PERSONNEL`: Military: Military personnel - `MILITARY_MILITARY_AIRCRAFT`: Military: Military aircraft - `MILITARY_WEAPONS_AND_EQUIPMENT`: Military: Weapons and equipment - `MILITARY_OTHER`: Military: Other - `HEALTH`: Health (all subcategories) - `HEALTH_SEXUAL_HEALTH`: Health: Sexual health - `HEALTH_TRADITIONAL_CHINESE_MEDICINE`: Health: Traditional Chinese medicine - `HEALTH_HEALTH_EDUCATION`: Health: Health education - `HEALTH_WELLNESS`: Health: Wellness - `HEALTH_MEDICAL_CARE`: Health: Medical care - `HEALTH_ORAL_HEALTH`: Health: Oral health - `HEALTH_WOMENS_HEALTH`: Health: Women's health - `HEALTH_MENTAL_HEALTH`: Health: Mental health - `HEALTH_MENS_HEALTH`: Health: Men's health - `HEALTH_DISEASE_PREVENTION_AND_TREATMENT`: Health: Disease prevention and treatment - `HEALTH_CANCER`: Health: Cancer - `HEALTH_OLDER_ADULT_HEALTH`: Health: Older adult health - `HEALTH_MEDICINES`: Health: Medicines - `HEALTH_DIETARY_HEALTH`: Health: Dietary health - `HEALTH_OTHER`: Health: Other - `SPORTS`: Sports (all subcategories) - `SPORTS_CBA`: Sports: CBA - `SPORTS_NBA`: Sports: NBA - `SPORTS_FITNESS`: Sports: Fitness - `SPORTS_WINTER_SPORTS`: Sports: Winter sports - `SPORTS_DOMESTIC_FOOTBALL`: Sports: Domestic football - `SPORTS_INTERNATIONAL_FOOTBALL`: Sports: International football - `SPORTS_MAJOR_SPORTS_EVENTS`: Sports: Major sports events - `SPORTS_LOTTERIES`: Sports: Lotteries - `SPORTS_OUTDOOR_SPORTS`: Sports: Outdoor sports - `SPORTS_COMBAT_SPORTS`: Sports: Combat sports - `SPORTS_EXTREME_SPORTS`: Sports: Extreme sports - `SPORTS_BOARD_AND_CARD_GAMES`: Sports: Board and card games - `SPORTS_YOGA`: Sports: Yoga - `SPORTS_OTHER_BASKETBALL`: Sports: Other basketball - `SPORTS_ELITE_SPORTS`: Sports: Elite sports - `SPORTS_GENERAL_SPORTS`: Sports: General sports - `SPORTS_OTHER_FOOTBALL`: Sports: Other football - `SPORTS_RUNNING`: Sports: Running - `SPORTS_FISHING`: Sports: Fishing - `SPORTS_OTHER`: Sports: Other - `AGRICULTURE_AND_RURAL_LIFE`: Agriculture and rural life (all subcategories) - `AGRICULTURE_AND_RURAL_LIFE_AGRICULTURE`: Agriculture and rural life: Agriculture - `AGRICULTURE_AND_RURAL_LIFE_RURAL_AREAS`: Agriculture and rural life: Rural areas - `AGRICULTURE_AND_RURAL_LIFE_FARMERS`: Agriculture and rural life: Farmers - `AGRICULTURE_AND_RURAL_LIFE_OTHER`: Agriculture and rural life: Other - `OTHER`: Other (all subcategories) - `OTHER_CONTENT`: Other: Other content
            fans_levels: Comma-separated preset follower-count ranges: below 5,000; 5,000-9,999; 10,000-19,999; 20,000-49,999; 50,000-99,999; 100,000-499,999; 500,000-999,999; or at least 1,000,000. Multiple selections are combined; leave unset for all follower counts.  Available Values: - `UNDER_5K`: Under 5,000 followers (0 through 4,999) - `FROM_5K_TO_10K`: 5,000 to under 10,000 followers (5,000 through 9,999) - `FROM_10K_TO_20K`: 10,000 to under 20,000 followers (10,000 through 19,999) - `FROM_20K_TO_50K`: 20,000 to under 50,000 followers (20,000 through 49,999) - `FROM_50K_TO_100K`: 50,000 to under 100,000 followers (50,000 through 99,999) - `FROM_100K_TO_500K`: 100,000 to under 500,000 followers (100,000 through 499,999) - `FROM_500K_TO_1M`: 500,000 to under 1 million followers (500,000 through 999,999) - `AT_LEAST_1M`: At least 1 million followers (1,000,000 through 4,294,967,295)
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/mp_publisher/search/v1",
            {
                "keyword": keyword,
                "page": page,
                "creatorTypes": creator_types,
                "fansLevels": fans_levels,
            },
        )

    def cgi_bin_advertiser_finder_publisher_detail_v1(
        self,
        *,
        app_id: str,
    ) -> ApiResponse[Any]:
        """
        Video Account Creator Details

        Retrieves QQ Huxuan Video Account creator details for a known creator app ID. Use it to review a shortlisted video creator before Tencent Huxuan campaign selection.

        Args:
            app_id: Video Account creator app ID.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/finder_publisher/detail/v1",
            {
                "appId": app_id,
            },
        )

    def cgi_bin_advertiser_finder_publisher_get_finder_video_show_v1(
        self,
        *,
        app_id: str,
        begin_date: str,
        end_date: str,
        video_type: str | None = "ALL",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Video Account Recent Videos

        Lists videos from a QQ Huxuan Video Account creator within a required date range, with a choice of all, Huxuan order, hot, or personal videos. Use it to review a shortlisted creator's content for campaign planning.

        Args:
            app_id: Video Account creator app ID.
            begin_date: Start date in yyyyMMdd format.
            end_date: End date in yyyyMMdd format.
            video_type: Tencent Huxuan video type filter.  Available Values: - `ALL`: All videos - `ORDER`: QQ Huxuan order videos - `HOT`: Hot videos - `PERSON`: Personal videos
            page: Page number. The first page is 1.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/finder_publisher/get_finder_video_show/v1",
            {
                "appId": app_id,
                "beginDate": begin_date,
                "endDate": end_date,
                "videoType": video_type,
                "page": page,
            },
        )

    def cgi_bin_advertiser_mp_publisher_detail_v1(
        self,
        *,
        app_id: str,
    ) -> ApiResponse[Any]:
        """
        Official Account Creator Details

        Retrieves QQ Huxuan Official Account creator details for a known creator app ID. Use it to review a shortlisted publisher before Tencent Huxuan campaign selection.

        Args:
            app_id: Official Account creator app ID.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/mp_publisher/detail/v1",
            {
                "appId": app_id,
            },
        )

    def cgi_bin_advertiser_mp_publisher_get_user_articles_v1(
        self,
        *,
        app_id: str,
        start_date: str,
        end_date: str,
        keyword: str | None = "",
        article_type: str | None = "ALL",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Official Account Article List

        Lists articles from a QQ Huxuan Official Account creator within a required date range, with an optional title keyword and a choice between all articles and Huxuan order articles. Use it to review a publisher's content for campaign planning.

        Args:
            app_id: Official Account creator app ID.
            start_date: Start date in yyyyMMdd format.
            end_date: End date in yyyyMMdd format.
            keyword: Article title keyword. Leave empty to return all matched articles.
            article_type: Tencent Huxuan article type filter.  Available Values: - `ALL`: All articles - `ORDER`: QQ Huxuan order articles
            page: Page number. The first page is 1.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/mp_publisher/get_user_articles/v1",
            {
                "appId": app_id,
                "startDate": start_date,
                "endDate": end_date,
                "keyword": keyword,
                "articleType": article_type,
                "page": page,
            },
        )

    def cgi_bin_advertiser_finder_publisher_get_rank_finder_content_v1(
        self,
        *,
        category: str | None = "ALL",
        sort: str | None = "INTERACTION",
        month: str | None = None,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Hot Content Trends

        Lists QQ Huxuan hot Video Account content by month and creator category, with six descending sort metrics and page-number pagination. Use it to research monthly content trends for Tencent Huxuan campaign planning.

        Args:
            category: Creator category. ALL includes every category.  Available Values: - `ALL`: All creator categories - `FOOD`: Food - `LIFESTYLE`: Lifestyle - `COMEDY`: Comedy - `EMOTION`: Emotion and relationships - `SOCIETY`: Society - `HUMANITIES_ARTS`: Humanities and arts - `DRAMA`: Drama - `ENTERTAINMENT`: Entertainment - `TECHNOLOGY`: Technology - `FINANCE`: Finance - `FILM_TV_VARIETY`: Film, television and variety shows - `GAMING`: Gaming - `PARENTING`: Parenting - `MUSIC`: Music - `TRAVEL`: Travel - `SPORTS`: Sports - `SCIENCE`: Science education - `AUTOMOTIVE`: Automotive - `EDUCATION`: Education - `CAREER`: Career - `HEALTH`: Health - `PETS`: Pets
            sort: Sort metric. Results are sorted in descending order.  Available Values: - `INTERACTION`: Interaction count - `PLAY`: Play count - `THUMB_LIKE`: Thumbs-up like count - `HEART_LIKE`: Heart like count - `COMMENT`: Comment count - `SHARE`: Share count
            month: Statistics month in yyyy-MM format. Omit to use the latest month available on QQ Huxuan.
            page: Page number, starting at 1. Each page contains up to 48 items.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/finder_publisher/get_rank_finder_content/v1",
            {
                "category": category,
                "sort": sort,
                "month": month,
                "page": page,
            },
        )
