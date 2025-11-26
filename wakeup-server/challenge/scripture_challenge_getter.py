import random
import json
from .challenge_getter import ChallengeGetter


class ScriptureChallengeGetter(ChallengeGetter):
    def __init__(self):
        self.scriptures = scriptures = [
            {
                "reference": "Isaiah 48:12-13",
                "text": """12 Hearken unto me, O Jacob and Israel, my called; I am he; I am the first, I also am the last.
13 Mine hand also hath laid the foundation of the earth, and my right hand hath spanned the heavens: when I call unto them, they stand up together."""
            },
            {
                "reference": "Isaiah 48:16-17",
                "text": """16 Come ye near unto me, hear ye this; I have not spoken in secret from the beginning; from the time that it was, there am I: and now the Lord God, and his Spirit, hath sent me.
17 Thus saith the Lord, thy Redeemer, the Holy One of Israel; I am the Lord thy God which teacheth thee to profit, which leadeth thee by the way that thou shouldest go."""
            },
            {
                "reference": "Isaiah 49:5-6",
                "text": """5 And now, saith the Lord that formed me from the womb to be his servant, to bring Jacob again to him, Though Israel be not gathered, yet shall I be glorious in the eyes of the Lord, and my God shall be my strength.
6 And he said, It is a light thing that thou shouldest be my servant to raise up the tribes of Jacob, and to restore the preserved of Israel: I will also give thee for a light to the Gentiles, that thou mayest be my salvation unto the end of the earth."""
            },
            {
                "reference": "Isaiah 49:8-11",
                "text": """8 Thus saith the Lord, In an acceptable time have I heard thee, and in a day of salvation have I helped thee: and I will preserve thee, and give thee for a covenant of the people, to establish the earth, to cause to inherit the desolate heritages;
9 That thou mayest say to the prisoners, Go forth; to them that are in darkness, Shew yourselves. They shall feed in the ways, and their pastures shall be in all high places.
10 They shall not hunger nor thirst; neither shall the heat nor sun smite them: for he that hath mercy on them shall lead them, even by the springs of water shall he guide them.
11 And I will make all my mountains a way, and my highways shall be exalted."""
            },
            {
                "reference": "Isaiah 49:13-16",
                "text": """13 Sing, O heavens; and be joyful, O earth; and break forth into singing, O mountains: for the Lord hath comforted his people, and will have mercy upon his afflicted.
14 But Zion said, The Lord hath forsaken me, and my Lord hath forgotten me.
15 Can a woman forget her sucking child, that she should not have compassion on the son of her womb? yea, they may forget, yet will I not forget thee.
16 Behold, I have graven thee upon the palms of my hands; thy walls are continually before me."""
            },
            {
                "reference": "Isaiah 49:22-23",
                "text": """22 Thus saith the Lord God, Behold, I will lift up mine hand to the Gentiles, and set up my standard to the people: and they shall bring thy sons in their arms, and thy daughters shall be carried upon their shoulders.
23 And kings shall be thy nursing fathers, and their queens thy nursing mothers: they shall bow down to thee with their face toward the earth, and lick up the dust of thy feet; and thou shalt know that I am the Lord: for they shall not be ashamed that wait for me."""
            },
            {
                "reference": "Isaiah 49:24-26",
                "text": """24 Shall the prey be taken from the mighty, or the lawful captive delivered?
25 But thus saith the Lord, Even the captives of the mighty shall be taken away, and the prey of the terrible shall be delivered: for I will contend with him that contendeth with thee, and I will save thy children.
26 And I will feed them that oppress thee with their own flesh; and they shall be drunken with their own blood, as with sweet wine: and all flesh shall know that I the Lord am thy Saviour and thy Redeemer, the mighty One of Jacob."""
            },
            {
                "reference": "Isaiah 50:1-4",
                "text": """1 Thus saith the Lord, Where is the bill of your mother’s divorcement, whom I have put away? or which of my creditors is it to whom I have sold you? Behold, for your iniquities have ye sold yourselves, and for your transgressions is your mother put away.
2 Wherefore, when I came, was there no man? when I called, was there none to answer? Is my hand shortened at all, that it cannot redeem? or have I no power to deliver? behold, at my rebuke I dry up the sea, I make the rivers a wilderness: their fish stinketh, because there is no water, and dieth for thirst.
3 I clothe the heavens with blackness, and I make sackcloth their covering.
4 The Lord God hath given me the tongue of the learned, that I should know how to speak a word in season to him that is weary: he wakeneth morning by morning, he wakeneth mine ear to hear as the learned."""
            },
            {
                "reference": "Isaiah 50:5-7",
                "text": """5 The Lord God hath opened mine ear, and I was not rebellious, neither turned away back.
6 I gave my back to the smiters, and my cheeks to them that plucked off the hair: I hid not my face from shame and spitting.
7 For the Lord God will help me; therefore shall I not be confounded: therefore have I set my face like a flint, and I know that I shall not be ashamed."""
            },
            {
                "reference": "Isaiah 51:1-3",
                "text": """1 Hearken to me, ye that follow after righteousness, ye that seek the Lord: look unto the rock whence ye are hewn, and to the hole of the pit whence ye are digged.
2 Look unto Abraham your father, and unto Sarah that bare you: for I called him alone, and blessed him, and increased him.
3 For the Lord shall comfort Zion: he will comfort all her waste places; and he will make her wilderness like Eden, and her desert like the garden of the Lord; joy and gladness shall be found therein, thanksgiving, and the voice of melody."""
            },
            {
                "reference": "Isaiah 51:4-5",
                "text": """4 Hearken unto me, my people; and give ear unto me, O my nation: for a law shall proceed from me, and I will make my judgment to rest for a light of the people.
5 My righteousness is near; my salvation is gone forth, and mine arms shall judge the people; the isles shall wait upon me, and on mine arm shall they trust."""
            },
            {
                "reference": "Isaiah 51:11-13",
                "text": """11 Therefore the redeemed of the Lord shall return, and come with singing unto Zion; and everlasting joy shall be upon their head: they shall obtain gladness and joy; and sorrow and mourning shall flee away.
12 I, even I, am he that comforteth you: who art thou, that thou shouldest be afraid of a man that shall die, and of the son of man which shall be made as grass;
13 And forgettest the Lord thy maker, that hath stretched forth the heavens, and laid the foundations of the earth; and hast feared continually every day because of the fury of the oppressor, as if he were ready to destroy? and where is the fury of the oppressor?"""
            },
            {
                "reference": "Isaiah 51:15-16",
                "text": """15 But I am the Lord thy God, that divided the sea, whose waves roared: The Lord of hosts is his name.
16 And I have put my words in thy mouth, and I have covered thee in the shadow of mine hand, that I may plant the heavens, and lay the foundations of the earth, and say unto Zion, Thou art my people."""
            },
            {
                "reference": "Isaiah 51:22-23",
                "text": """22 Thus saith thy Lord the Lord, and thy God that pleadeth the cause of his people, Behold, I have taken out of thine hand the cup of trembling, even the dregs of the cup of my fury; thou shalt no more drink it again:
23 But I will put it into the hand of them that afflict thee; which have said to thy soul, Bow down, that we may go over: and thou hast laid thy body as the ground, and as the street, to them that went over."""
            },
            {
                "reference": "Isaiah 52:1-3",
                "text": """1 Awake, awake; put on thy strength, O Zion; put on thy beautiful garments, O Jerusalem, the holy city: for henceforth there shall no more come into thee the uncircumcised and the unclean.
2 Shake thyself from the dust; arise, and sit down, O Jerusalem: loose thyself from the bands of thy neck, O captive daughter of Zion.
3 For thus saith the Lord, Ye have sold yourselves for nought; and ye shall be redeemed without money."""
            },
            {
                "reference": "Isaiah 52:7-8",
                "text": """7 How beautiful upon the mountains are the feet of him that bringeth good tidings, that publisheth peace; that bringeth good tidings of good, that publisheth salvation; that saith unto Zion, Thy God reigneth!
8 Thy watchmen shall lift up the voice; with the voice together shall they sing: for they shall see eye to eye, when the Lord shall bring again Zion."""
            },
            {
                "reference": "Isaiah 52:9-10",
                "text": """9 Break forth into joy, sing together, ye waste places of Jerusalem: for the Lord hath comforted his people, he hath redeemed Jerusalem.
10 The Lord hath made bare his holy arm in the eyes of all the nations; and all the ends of the earth shall see the salvation of our God."""
            },
            {
                "reference": "Isaiah 52:11-12",
                "text": """11 Depart ye, depart ye, go ye out from thence, touch no unclean thing; go ye out of the midst of her; be ye clean, that bear the vessels of the Lord.
12 For ye shall not go out with haste, nor go by flight: for the Lord will go before you; and the God of Israel will be your rearward."""
            },
            {
                "reference": "Isaiah 53:2-5",
                "text": """2 For he shall grow up before him as a tender plant, and as a root out of a dry ground: he hath no form nor comeliness; and when we shall see him, there is no beauty that we should desire him.
3 He is despised and rejected of men; a man of sorrows, and acquainted with grief: and we hid as it were our faces from him; he was despised, and we esteemed him not.
4 Surely he hath borne our griefs, and carried our sorrows: yet we did esteem him stricken, smitten of God, and afflicted.
5 But he was wounded for our transgressions, he was bruised for our iniquities: the chastisement of our peace was upon him; and with his stripes we are healed."""
            },
            {
                "reference": "Isaiah 53:6-7",
                "text": """6 All we like sheep have gone astray; we have turned every one to his own way; and the Lord hath laid on him the iniquity of us all.
7 He was oppressed, and he was afflicted, yet he opened not his mouth: he is brought as a lamb to the slaughter, and as a sheep before her shearers is dumb, so he openeth not his mouth."""
            },
            {
                "reference": "Isaiah 53:10-12",
                "text": """10 Yet it pleased the Lord to bruise him; he hath put him to grief: when thou shalt make his soul an offering for sin, he shall see his seed, he shall prolong his days, and the pleasure of the Lord shall prosper in his hand.
11 He shall see of the travail of his soul, and shall be satisfied: by his knowledge shall my righteous servant justify many; for he shall bear their iniquities.
12 Therefore will I divide him a portion with the great, and he shall divide the spoil with the strong; because he hath poured out his soul unto death, and he was numbered with the transgressors; and he bare the sin of many, and made intercession for the transgressors."""
            }
        ]

    def get_challenge(self):
        scripture = random.choice(self.scriptures)
        return json.dumps(scripture)
