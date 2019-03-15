from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Gadget, Base, MenuItem, User

engine = create_engine('sqlite:///gadgetdata.db')
"""Bind the engine to the metadata of the Base class so that the
declaratives can be accessed through a DBSession instance"""
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
"""A DBSession() instance establishes all conversations with the database
 and represents a "staging zone" for all the objects loaded into the
 database session object. Any change made against the objects in the
 session won't be persisted into the database until you call
 session.commit(). If you're not happy about the changes, you can
 revert all of them back to the last commit by calling
 session.rollback()"""
session = DBSession()
"""Create First User"""
User1 = User(name="Shyam Prasad", email="sp6163@gmail.com",
             picture='https://lh3.googleusercontent.com'
             '/-1nN0oMGaJuE/AAAAAAAAAAI/AAAAAAAAEJI/'
             'ztxtz9Y6R_4/s60-p-rw-no-il/photo.jpg')
session.add(User1)
session.commit()

"""Menu for Mobiles"""
gadget1 = Gadget(user_id=1, name="Mobile")
session.add(gadget1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="VIVO V11",
                     description='''Vivo, the innovative global smartphone brand,
                     today launched the V11 Pro in India,
                     complete with additional flagship
                     features such as the Pop-up selfie
                     camera,AI TripleRear Camera,
                     In-Display Fingerprint Technology and
                     Super AMOLED display in the
                     V series. With an almost bezel-less
                     91.64% screen-to-body ratio
                     and benchmark-setting features,
                     the smartphone will be available in 6GB + 128GB.''',
                     price="$354.214",
                     picture="http://tinyurl.com/yx976pek",
                     gadget=gadget1)
session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Samsung J7 Pro",
                     description='''Samsung Galaxy J7 16GB(White) with real 4G experience
                     with Ultra Data Saving, Vivid
                     & Immersive Viewing Experience,
                     Power Packed Performance.
                     Capture your best the stage is set.
                     Capture it brilliantly with the powerful
                     13 MP front & rear cameras on the Galaxy J7 Pro.
                     7 lens captures bright pictures
                     even in low-light conditions.''',
                     price="$263.948",
                     picture="http://tinyurl.com/y5uxjqp8",
                     gadget=gadget1)
session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="OnePlus 6T",
                     description='''Featuring our largest display ever and a
                     resilient glass back, the OnePlus
                     6T was crafted with
                     care and purpose. Experience a
                     6.41 inch Optic AMOLED display
                     for true immersion through an
                     86% screen-to-body ratio
                     beautifully slim cut-out.''',
                     price="$1576.35",
                     picture="http://tinyurl.com/y4pwsso4",
                     gadget=gadget1)
session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Apple iPhone Xs Max",
                     description='''Super Retina in two sizes including the largest
                     display ever on an iPhone. Even
                     faster Face ID. The smartest,
                     most powerful chip in a smartphone.
                     And a breakthrough dual-camera
                     system with Depth Control. iPhone XS
                     is everything you love about iPhone.''',
                     price="$746.881",
                     picture="http://tinyurl.com/y5seqk2z",
                     gadget=gadget1)
session.add(menuItem2)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Cat S61",
                     description='''Get the Cat S61 smartphone
                     to make your work easier.
                     With an integrated thermal imaging
                     camera, indoor air quality sensor,
                     and laser assisted distance measurement,
                     you can take on anything.
                     Measure distances and area using the Measure
                     app on the Cat S61.
                     Safely document measurements
                     and record the layout of an area all
                     in one screen, helping to make work
                     estimates quicker and easier.''',
                     price="$899.99",
                     picture="http://tinyurl.com/yxgpuao8",
                     gadget=gadget1)
session.add(menuItem2)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Samsung Galaxy Note9 SM-N960U",
                     description='''The result of 10 years of
                     \pioneering mobile firsts,
                     Galaxy S10e, S10, and S10 introduce the next
                     generation of mobile innovation.
                     Galaxy S10e, S10, and S10. The next generation
                     of Galaxy has arrived.Completely redesigned
                     to remove interruptions from your view.
                     No notch, no distractions.
                     Precise laser cutting, on-screen security,
                     and a Dynamic AMOLED that's easy
                     on the eyes make the Infinity O Display the
                     most innovative Galaxy screen yet.''',
                     price="$1149.00",
                     picture="http://tinyurl.com/y4xn4d23",
                     gadget=gadget1)
session.add(menuItem2)
session.commit()


"""Menu for LapTops"""
gadget2 = Gadget(user_id=1, name="Lap Tops")
session.add(gadget2)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Samsung Notebook 9 Pro",
                     description='''Samsung Notebook 9 Pen is engineered for
                     people who are going places. Count
                     on exceptional processing
                     power and fast charging to keep
                     you moving forward and
                     a lightweight frame that wont
                     weigh you down.
                     Samsung Notebook 9 may be
                     stunningly light,
                     but when it comes to performance,
                     its anything but a lightweight.''',
                     price="$1234.56",
                     picture="http://tinyurl.com/y48azuwb",
                     gadget=gadget2)
session.add(menuItem1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Dell Inspiron Core i5 8th Gen",
                     description='''Dell empowers countries, communities,
                     customers and people everywhere
                     to use technology to
                     realize their dreams. Customers
                     trust us to deliver technology
                     solutions that help them do and achieve
                     more, whether they are at home,
                     work, school or anywhere in their world.
                     Learn more about our story,
                     purpose and people behind our
                     customer-centric approach.''',
                     price="$932.32",
                     picture="http://tinyurl.com/y3g8dpxg",
                     gadget=gadget2)
session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="ASUS ZenBook 15 Ultra-SlimCompact",
                     description='''ASUS became widely known in
                     North America when it
                     revolutionized the PC industry in
                     2007 with its Eee PC.
                     Today, the company is pioneering
                     new mobile trends with the ASUS ZenFone
                     series, and it is rapidly developing
                     virtual and augmented reality products
                     as well as IOT devices and robotics
                     technologies. Most recently,
                     ASUS introduced Zenbo, a smart
                     home robot designed to provide
                     assistance, entertainment, and
                     companionship to families.''',
                     price="$1432.38",
                     picture="http://tinyurl.com/y4d8ye45",
                     gadget=gadget2)
session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="ACER AspireSwitch10e",
                     description='''With its thin, premium
                     aluminum design,
                     this laptops got looks and
                     mobility.
                     The hairline brushed pattern
                     provides an exquisite,
                     tactile finish accenting the
                     premium aluminum cover.
                     Travel with ease and look
                     great doing it.
                     The narrow, 7.82mm1 bezel design
                     offers more real estate for amazing
                     images. With a 15.6 FHD IPS
                     display and Acer Color
                     Intelligence1 crisp, true to
                     life colors come alive.
                     Adjust gamma and saturation
                     in real time, optimizing
                     screen color and brightness
                     without clipping.''',
                     price="$746.881",
                     picture="http://tinyurl.com/yyfa9z3p",
                     gadget=gadget2)
session.add(menuItem2)
session.commit()

menuItem2 = MenuItem(user_id=1, name="HP Pavilion x360",
                     description='''Ultra-slim styles, cutting edge security and
                     crystal-clear collaboration features
                     keep you productive anywhere.
                     Enhanced with a range of
                     security features and built
                     for business with durability
                     and connectivity options.
                     Work, write or play naturally
                     with a durable 360 degree hinge,
                     liberating battery life and 8th
                     generation Intel Core processors.''',
                     price="$981.302",
                     picture="http://tinyurl.com/y4ux56zz",
                     gadget=gadget2)
session.add(menuItem2)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Lenovo Ideapad 530s",
                     description='''Lenovo Laptops with 8th Gen
                     Intel Core and Windows 10
                     for Work and Entertainment.
                     Buy Now. Convertible Laptop.
                     Exciting Deals. Detachable Keyboard.
                     Dolby Advanced Audio. Easy
                     Payment Options.
                     Exclusive Online Models. Unique Colors.
                     Exquisite Colours. Light Weight. Ample storage.''',
                     price="$917.955",
                     picture="http://tinyurl.com/y2qxehyl",
                     gadget=gadget2)
session.add(menuItem2)
session.commit()

"""MenuforRefrigerator"""
gadget3 = Gadget(user_id=1, name="Refrigerators")
session.add(gadget3)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Whirlpool 330 L Multi-Door Refrigerator",
                     description='''In 1995 Whirlpool acquired
                     Kelvinator India Limited
                     and marked an entry into the
                     refrigerator market as well.
                     The same year the company also
                     saw acquisition of major
                     shares in TVS joint venture
                     and later in 1996, Kelvinator
                     and TVS acquisitions were merged
                     to create, Whirlpool of India
                     Limited. This expanded the companys
                     portfolio in the Indian subcontinent
                     to washing machines, refrigerator,
                     microwave ovens and air conditioners.''',
                     price="$542.50",
                     picture="http://tinyurl.com/y3xvsyms",
                     gadget=gadget3)
session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Haier 190 L 3",
                     description='''Haiers revenues have
                     shot up fourfold
                     since 2000 with an annual
                     Group turnover of 180.3
                     billion yuan, US $ 29.5 billion.
                     Haier has 24 industrial parks,
                     5 R&D centers, 66 trading companies,
                     143330 sales outlets and
                     more than 70,000 employees
                     around the world.
                     The product range comprises of
                     over 15,100 models in 96 categories''',
                     price="$210.99",
                     picture="http://tinyurl.com/y39tgmbn",
                     gadget=gadget3)
session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Mitashi 46 L 2 Star",
                     description='''Interlinking hearts and
                     synchronizing emotions,
                     we, at Mitashi weave a dream with
                     every creation of ours.
                     Making the recipe of life the most
                     tingling to our senses,
                     we add the unique ingredients of
                     , entertainment,
                     innovation, creativity, feelings and
                     dedication to serve you
                     the best of the products, manufactured
                     with detailed precision.''',
                     price="$145.99",
                     picture="https://tinyurl.com/yydd4jeh",
                     gadget=gadget3)
session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="LG 190 L 4 Star ",
                     description='''We are reaching out to discerning
                     consumers with keen sensibilities
                     people who continue to
                     explore new activities
                     and take on new challenges to
                     experience more and achieve
                     a better life. We have developed
                     our brand image gradually
                     and consistently, always to
                     communicate, Lifes Good.
                     We are contemporary yet authentic,
                     always evolving
                     our fundamental philosophies
                     to the modern arena.''',
                     price="$231.68",
                     picture="https://tinyurl.com/yyve2s4y",
                     gadget=gadget3)
session.add(menuItem2)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Samsung 253 L Frost",
                     description='''The Samsung Food ShowCase
                     Refrigerator
                     is designed to improve the
                     way you store food through
                     an innovative 2 Door system.We
                     look forward to exploring new
                     business areas such as healthcare
                     and automotive electronics,
                     and continue our journey through
                     history of innovation.
                     Samsung Electronics will
                     welcome new challenges
                     and opportunities with joy.''',
                     price="$432.421",
                     picture="https://tinyurl.com/y2pvqnoe",
                     gadget=gadget3)
session.add(menuItem2)
session.commit()

menuItem2 = MenuItem(user_id=1, name="BPL 564 L Frost ",
                     description='''Classy and elegant,
                     the black glass finish
                     adds to the luxe
                     interiors of your kitchen.
                     Ultra- quick cooling and
                     super freeze mode
                     (ice is ready at the snap
                     of a finger) keeps you
                     party-ready at all times.''',
                     price="$632.921",
                     picture="https://tinyurl.com/y3msoyy2",
                     gadget=gadget3)
session.add(menuItem2)
session.commit()
"""Menu for Television"""
gadget4 = Gadget(user_id=1, name="Television")
session.add(gadget4)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Sony Bravia 4K UHD LED",
                     description='''An ordinary moment turns
                     into a memorable one,
                     when the best experiences
                     come together.
                     BRAVIA with its path breaking
                     technologies ensures
                     that you live these
                     moments every day.
                     It makes the most gorgeous
                     images shine with perfect details,
                     spectacular colours
                     and striking contrast.
                     Get closest to reality with
                     Sonys unique technologies.''',
                     price="$231.78",
                     picture="https://tinyurl.com/y5q9eckr",
                     gadget=gadget4)
session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Mi LED Smart TV 4A 32",
                     description='''Mi knowledgeable staff
                     provides you with a comprehensive
                     product consultation and helps you
                     to buy a product which fits your needs.
                     Whether it be product specification,
                     operational guidance, or an unsettling
                     urge to deep dive and
                     understand the product even better,
                     MI team will answer all
                     of them, one by one.''',
                     price="$167.99",
                     picture="https://tinyurl.com/y6qpnqmh",
                     gadget=gadget4)
session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Daiwa L42FVC4U",
                     description='''By investing a lot of time,
                     knowledge and expertise on the
                     manufacture and production of high
                     quality LED TVs, Daiwa is frequently at
                     the forefront of new, ground-breaking
                     concepts. Daiwa products are manufactured
                     on a specially developed production
                     line based in NOIDA.
                     DAIWA TVs are assembled
                     to exact specifications in
                     order to ensure that
                     every single LED TV is produced
                     to the highest standard.''',
                     price="$142.99",
                     picture="https://tinyurl.com/y26xhfy8",
                     gadget=gadget4)
session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Panasonic TH-40F200DX",
                     description='''Panasonic is a name that
                     needs no introduction.
                     Offering a wide range of home appliances
                     and consumer electronics,
                     Panasonic is a class apart. Standing tall
                     amidst the likes of Sony, Samsung,
                     LG and other electronic giants, this Japanese
                     company has been liked across
                     the world for being technology oriented and
                     delivering exceptional customer
                     services.''',
                     price="$193.50",
                     picture="https://tinyurl.com/y4zt9swp",
                     gadget=gadget4)
session.add(menuItem2)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Samsung 4k Smart TV",
                     description='''Samsung 4k Ultra HD looks
                     sharp, crisp images with 4K UHD TV that
                     has 4x more pixels than a FHD TV.
                     Now you can see even the
                     smallest details in every scene.
                     Innovative Tune Station will
                     add visual experience to your\
                     playlist by turning your TV
                     into a virtual music system.''',
                     price="$624.99",
                     picture="https://tinyurl.com/y4dcndzu",
                     gadget=gadget4)
session.add(menuItem2)
session.commit()

menuItem2 = MenuItem(user_id=1, name="LG Smart TV",
                     description='''This new range of TVs take the
                     special qualities of webOS
                     to an even larger level of entertainment
                     so that one can get the most out
                     of their primetime viewing experience.
                     LG WebOS TV is designed to be simple
                     enough to learn and fun to use.''',
                     price="$242.54",
                     picture="https://tinyurl.com/y4saeks9",
                     gadget=gadget4)
session.add(menuItem2)
session.commit()

print("added menu items!")
