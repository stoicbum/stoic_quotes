from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Stoics, Base, Quote

engine = create_engine('sqlite:///stoic.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#quotes for Marcus Aurelius
stoic1 = Stoics(name="Marcus Aurelius")

session.add(stoic1)
session.commit()

quote1 = Quote(quote="Your mind will take the shape of what you frequently hold in thought, for the human spirit is colored by such impressions.", stoic = stoic1)
session.add(quote1)
session.commit()

quote2 = Quote(quote = "Waste no more time arguing what a good man should be--be one.", stoic= stoic1)
session.add(quote2)
session.commit()

quote3 = Quote(quote= "When you are distressed by an external thing, it's not the thing itself that troubles you, but only your judgement of it. And you can wipe this out at a moments notice.", stoic = stoic1)
session.add(quote3)
session.commit()

quote4= Quote(quote = "If we judge as good and evil only the things in the power of our own choice, then there is no room left for blaming gods or being hostile to others.", stoic= stoic1)
session.add(quote4)
session.commit()

quote5 = Quote(quote = "This is the mark of perfection of character--to spend each day as if it were your last, without frenzy, laziness, or any pretending.", stoic = stoic1)
session.add(quote5)
session.commit()

quote6 = Quote(quote = "You get what you deserve. Instead of being a good person today, you choose instead to become one tomorrow.", stoic = stoic1)
session.add(quote6)
session.commit()

quote7 = Quote(quote= "Pay attention to what's in front of you--the principle, the task, or what's being portrayed.", stoic= stoic1)
session.add(quote7)
session.commit()

quote8 = Quote(quote = "These are the characteristics of the rational soul: self-awareness, self-examination, and self-determination. It reaps its own harvest... It succeeds in its own purpose.", stoic = stoic1)
session.add(quote8)
session.commit()

quote9 = Quote(quote= "Take a good hard look at people's ruling principle, especially of the wise, what they run away from what they seek out.", stoic=stoic1)
session.add(quote9)
session.commit()

quote10 = Quote(quote ="Receive without pride, let go without attachment.", stoic = stoic1)
session.add(quote10)
session.commit()
#quotes from Seneca
stoic2 = Stoics(name="Seneca")
session.add(stoic2)
session.commit()

quote1 = Quote(quote = "We should take wandering outdoor walks, so that the mind might be nourished and refreshed by the air and deep breathing.", stoic = stoic2)
session.add(quote1)
session.commit()

quote2 = Quote(quote= "Think of those who, not by fault of inconsistency but by lack of effort, are too unstable to live as they wish, but only live as tey have begun.", stoic = stoic2)
session.add(quote2)
session.commit()

quote3 = Quote(quote = "Work nourishes noble minds.", stoic = stoic2)
session.add(quote3)
session.commit()

quote4 = Quote(quote = "If a man knows not which port he sails, no wind is favorable.", stoic = stoic2)
session.add(quote4)
session.commit()

quote5 = Quote(quote = "We are more often frightened than hurt; and we suffer more in imagination than in reality.", stoic = stoic2)
session.add(quote5)
session.commit()

quote6 = Quote(quote="People are frugal in guarding their personal property; but as soon as it comes to squandering tim ethey are most wasteful of the one thing in which it is right to be stingy.", stoic= stoic2)
session.add(quote6)
session.commit()

quote7 = Quote(quote = "No person has the power to have everything they want, but it is in their power not to want what they do not have, and to cheerfully put to good use what they do have.", stoic = stoic2)
session.add(quote7)
session.commit()

quote8 = Quote(quote = "Life is very short and anxious for those who forget the past, neglect the present, and fear the future.", stoic = stoic2)
session.add(quote8)
session.commit()

quote9 = Quote(quote = "He who fears death will never do anything worth of a man who is alive.", stoic = stoic2)
session.add(quote9)
session.commit()
#quotes from Epictetus
stoic3 = Stoics(name="Epictetus")
session.add(stoic3)
session.commit()

quote1 = Quote(quote = "First say to yourself what you would be; and then do what you have to do.", stoic = stoic3)
session.add(quote1)
session.commit()

quote2 = Quote(quote = "Curb your desire, do not set your heart on so many things and you will get what you need.", stoic = stoic3)
session.add(quote2)
session.commit()

quote3 = Quote(quote = "Do not explain your philosophy. Embody it.", stoic = stoic3)
session.add(quote3)
session.commit()

quote4 = Quote(quote = "If anyone tells you that a certain person speaks ill of you, do not make excuses about what is said of you but answer, He was ignorant of my other faults, else he would have not mentioned these alone.", stoic = stoic3)
session.add(quote4)
session.commit()

quote5 = Quote(quote = "Freedom is the only worthy goal in life. It is won by disregarding things that lie beyond our control.", stoic = stoic3)
session.add(quote5)
session.commit()

quote6 = Quote(quote = "When anyone seems to be provoking you, remember that it is only your judgemnet of the incident that provokes you. Don't let your emotions get ignited by mere appearances.", stoic = stoic3)
session.add(quote6)
session.commit()

quote7 = Quote(quote = "As you think, so you become.", stoic = stoic3)
session.add(quote7)
session.commit()

quote8 = Quote(quote ="Only the morally weak feel compelled to defend or explain themselves to others. Let the quality of your deeds speak on your behalf.", stoic = stoic3)
session.add(quote8)
session.commit()

quote9= Quote(quote = "When we succumb to whining, we diminish our possibilities.", stoic = stoic3)
session.add(quote9)
session.commit()
#quotes from Viktor Frankel
stoic4 = Stoics(name = "Viktor Frankel")
session.add(stoic4)
session.commit()

quote1 = Quote(quote = "What man actually needs is not a tensionless state but rather the striving and struggling for some goal worthy of him.", stoic = stoic4)
session.add(quote1)
session.commit()

quote2 = Quote(quote = "When we are no longer able to change a situation, we are challenged to change ourselves.", stoic = stoic4)
session.add(quote2)
session.commit()

print "added stoics and quotes!"










