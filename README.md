# Encrypter

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Encrypter testing](https://github.com/MaxsLi/Encrypter/actions/workflows/encrypter_testing.yml/badge.svg)](https://github.com/MaxsLi/Encrypter/actions/workflows/encrypter_testing.yml)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/maxsli/Encrypter?style=plastic)
![GitHub all releases](https://img.shields.io/github/downloads/MaxsLi/Encrypter/total)
![GitHub](https://img.shields.io/github/license/maxsli/Encrypter)

## Usage

The script can be executed in three different modes:

* **Normal**: Execute without any argument.
  * Enter an input for encryption, and the script will return the encrypted input.
  * Enter an encrypted input for decryption, and return the result.
  * Enter `R` (or `r`) to re-run the program, or anything else to exit.

* **Decrypt**: Execute with argument: `-d` followed by the string needed to be decrypted. Will decrypt the given encrypted string.
  * `./ED.py -d 'Encrypted_String'`
  * Noted the single quote characters surrounding the encrypted input, this is necessary because `Encrypted_String` contains special characters.

* **Encrypt**: Execute with argument: `-e` followed by the string needed to be encrypted. Will encrypt the given input string.
  * `./ED.py -e 'Input_String'`
  * Noted the single quote characters surrounding the input string.

For more examples, please visit [here](#examples).

```text
usage: ED.py [-h] [-d DECRYPT] [-e ENCRYPT]

optional arguments:
  -h, --help            show this help message and exit
  -d DECRYPT, --decrypt DECRYPT
                        Decrypt an encrypted string
  -e ENCRYPT, --encrypt ENCRYPT
                        Encrypt an input string
```

## Encrypting Process

Given input string:

* Generate a random `offset` number.
* For every `character` in the input string:
  * Generate a `random_letter`, a `random_number` and a `random_symbol`(Special Character).
  * Add these random elements to a list called `seed`.
  * Convert the `character` to ASCII code and add the `offset` to the ASCII code.
  * Add these random elements to a list called `code`.
* Then encrypt the list `seed` that we just created.
* Return combination of encrypted `seed` and input string.

## Decrypting Process

Given input cypher:

* Split the cypher to `encrypted_seed` and `encrypted_input`.
* Decrypt the `encrypted_seed` to `decrypted_seed`.
* For every `character` in the `encrypted_input`:
  * Check if the `character` is one of the `decrypted_seed`:
    * If so, go to the next character.
    * Otherwise, add it to a list for decrypt.
  * Convert the characters to be decrypted to ASCII code and minus the `offset`.
* Return the input string.

## Simple Illustration

Given a user input string `a`, the script returned the cypher as:

```text
47a3^X5}F8-V5-p1%*102a3^104X5}145F8-103V5-90p1%*176b8+*
```

Now, let's read this cypher from back to forth, note that the last character
is always the `separator`, and given this `separator`, we can divide the cypher
into two parts: `encrypted seed` and `encrypted input`:

```text
47a3^X5}F8-V5-p1%*102a3^104X5}145F8-103V5-90p1% * 176b8+ *
└───────────────────┬──────────────────────────┘│└───┬──┘│
             encrypted seed                separator │ separator
                                              encrypted input
```

Let's focus on the `encrypted seed`, which has the similar layout as the cypher we saw
above:

```text
47 a3^X5}F8-V5-p1% * 102a3^104X5}145F8-103V5-90p1% *
│  └──────┬──────┘ │ └────────────┬──────────────┘ │
offset  seed    separator        code           separator
```

Notice the `code` and the `seed`:

```text
    a3^     X5}     F8-     V5-    p1%         seed
     │       │       │       │       │
102 a3^ 104 X5} 145 F8- 103 V5- 90 p1%         code
 │       │       │       │      │
102     104     145     103     90
```

Remember the `offset` for the encrypted seed is `47`, hence we
subtract `47` from all these numbers:

```text
102 104 145 103 90
 │   │   │   │   │        Subtract 47
55  57  98  56  43
 │   │   │   │   │        ASCII
 7   9   b   8   +
```

We have successfully decrypted the `seed`, now its time for the `input`:

```text
47a3^X5}F8-V5-p1%*102a3^104X5}145F8-103V5-90p1% * 176b8+ *
└───────────────────┬──────────────────────────┘│└───┬──┘│
             encrypted seed                separator │ separator
             └─────┬─────┘                      encrypted input
               7 9 b 8 +
```

Replacing `encrypted seed` as `decrypted seed`, combining with `encrypted input`:

```text
79b8+  * 176b8+ *
└─┬──┘ │ └────┴─│─────────────────┐
  │ separator separator    encrypted input
decrypted seed
```

Breaking down:

```text
79 b8+ * 176b8+ *
 │  │  │ └────┴─│──────────┐
 │seed separator    encrypted input
offset
```

As we can see, the `encrypted input` is `176b8+` and the `seed` is `b8+`.

Hence removing `b8+` from `176b8+` we get `176`.

Then minus the offset `79`: `176-79 = 97`

Voila! `97` is the ASCII code for character `a`. We have successfully decrypted the input.

## Examples

```text
Enter: a
Encrypt: 87D6?U7}c9`y7/W1@)144D6?139U7}157c9`140y7/147W1@)191F5<)
Decrypt: a

./ED.py -d '87D6?U7}c9`y7/W1@)144D6?139U7}157c9`140y7/147W1@)191F5<)'
Decrypting: 87D6?U7}c9`y7/W1@)144D6?139U7}157c9`140y7/147W1@)191F5<)
Decrypted: a

./ED.py -e 1
Encrypting: 1
Encrypted: 12A8$S9:j1<q9=F0^(68A8$69S9:116j1<64q9=137F0^(138h4}(

Enter: 1
Encrypt: 91t7.k3@m3=z6,u0;(140t7.148k3@165m3=140z6,151u0;(68J1<(
Decrypt: 1

Enter: 1
Encrypt: 42g5?D0!I6+j1{B7;~94g5?94D0!123I6+95j1{79B7;~93Q5%~
Decrypt: 1

Enter: 1
Encrypt: 32d6#F7^p6-w5)X9);83d6#89F7^141p6-88w5)77X9);88m8-;
Decrypt: 1

Enter: Hello
Encrypt: 81s7&Z2[N9#x0<B6!V0`a4~c7]h1%o5<C1$g9*t6%P0.A3/H7}n2!{137s7&136Z2[200N9#133x0<176B6!199V0`131a4~125c7]190h1%135o5<139C1$186g9*138t6%128P0.180A3/131H7}117n2!{159w4_188v2,195m6:195i9/198c2${
Decrypt: Hello

Enter: 你好
Encrypt: 98G3$m4]r3~G2=x4(u9%n3<B2~+147G3$151m4]215r3~147G2=192x4(220u9%153n3<144B2~+20335u1^22924z7.+
Decrypt: 你好

Enter: こんにちは
Encrypt: 24S8.Y9$N5{z8)F6,u4,O8;e3$w3[q4.d1#f1?e8:L2,N0:r6$r4;^77S8.77Y9$106N5{78z8)120F6,139u4,76O8;115e3$135w3[79q4.71d1#121f1?74e8:88L2,92N0:73r6$62r4;^12426R6`12490s4[12450o7/12440a2@12454D1&^
Decrypt: こんにちは

Enter: γεια σας
Encrypt: 44w7;r9$j3#d1^B7,u0!j5!Y4+C4}Q7(u7>U0]C7}c9*e1^K1|O6/O4;U2^T6}S2?d3,v3&W4<O9>n1&%99w7;96r9$126j3#100d1^168B7,164u0!94j5!89Y4+163C4}94Q7(170u7>123U0]100C7}107c9*127e1^92K1|139O6/150O4;97U2^167T6}113S2?96d3,169v3&166W4<100O9>168n1&%1021R8|1023x2-1027w2~1019O8?106S0_1037j5{1019E4}1036z8|%
Decrypt: γεια σας

Enter: I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in the history of our nation. Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity. But one hundred years later, the Negro still is not free. One hundred years later, the life of the Negro is still sadly crippled by the manacles of segregation and the chains of discrimination. One hundred years later, the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity. One hundred years later, the Negro is still languishing in the corners of American society and finds himself an exile in his own land. So we have come here today to dramatize a shameful condition. In a sense we have come to our nation’s capital to cash a check. When the architects of our republic wrote the magnificent words of the Constitution and the Declaration of Independence, they were signing a promissory note to which every American was to fall heir. This note was a promise that all men, yes, black men as well as white men, would be guaranteed the unalienable rights of life, liberty, and the pursuit of happiness. It is obvious today that America has defaulted on this promissory note insofar as her citizens of color are concerned. Instead of honoring this sacred obligation, America has given the Negro people a bad check, a check which has come back marked “insufficient funds.” But we refuse to believe that the bank of justice is bankrupt. We refuse to believe that there are insufficient funds in the great vaults of opportunity of this nation. So we have come to cash this check — a check that will give us upon demand the riches of freedom and the security of justice. We have also come to this hallowed spot to remind America of the fierce urgency of now. This is no time to engage in the luxury of cooling off or to take the tranquilizing drug of gradualism. Now is the time to make real the promises of democracy. Now is the time to rise from the dark and desolate valley of segregation to the sunlit path of racial justice. Now is the time to lift our nation from the quick sands of racial injustice to the solid rock of brotherhood. Now is the time to make justice a reality for all of God’s children. It would be fatal for the nation to overlook the urgency of the moment. This sweltering summer of the Negro’s legitimate discontent will not pass until there is an invigorating autumn of freedom and equality. Nineteen sixty-three is not an end, but a beginning. Those who hope that the Negro needed to blow off steam and will now be content will have a rude awakening if the nation returns to business as usual. There will be neither rest nor tranquility in America until the Negro is granted his citizenship rights. The whirlwinds of revolt will continue to shake the foundations of our nation until the bright day of justice emerges. But there is something that I must say to my people who stand on the warm threshold which leads into the palace of justice. In the process of gaining our rightful place we must not be guilty of wrongful deeds. Let us not seek to satisfy our thirst for freedom by drinking from the cup of bitterness and hatred. We must forever conduct our struggle on the high plane of dignity and discipline. We must not allow our creative protest to degenerate into physical violence. Again and again we must rise to the majestic heights of meeting physical force with soul force. The marvelous new militancy which has engulfed the Negro community must not lead us to a distrust of all white people, for many of our white brothers, as evidenced by their presence here today, have come to realize that their destiny is tied up with our destiny. They have come to realize that their freedom is inextricably bound to our freedom. We cannot walk alone. As we walk, we must make the pledge that we shall always march ahead. We cannot turn back. There are those who are asking the devotees of civil rights, “When will you be satisfied?” We can never be satisfied as long as the Negro is the victim of the unspeakable horrors of police brutality. We can never be satisfied, as long as our bodies, heavy with the fatigue of travel, cannot gain lodging in the motels of the highways and the hotels of the cities. We cannot be satisfied as long as the Negro’s basic mobility is from a smaller ghetto to a larger one. We can never be satisfied as long as our children are stripped of their selfhood and robbed of their dignity by signs stating “For Whites Only”. We cannot be satisfied as long as a Negro in Mississippi cannot vote and a Negro in New York believes he has nothing for which to vote. No, no, we are not satisfied, and we will not be satisfied until 
justice rolls down like waters and righteousness like a mighty stream. I am not unmindful that some of you have come here out of great trials and tribulations. Some of you have come fresh from narrow jail cells. Some of you have come from areas where your quest for freedom left you battered by the storms of persecution and staggered by the winds of police brutality. You have been the veterans of creative suffering. Continue to work with the faith that unearned suffering is redemptive. Go back to Mississippi, go back to Alabama, go back to South Carolina, go back to Georgia, go back to Louisiana, go back to the slums and ghettos of our northern cities, knowing that somehow this situation can and will be changed. Let us not wallow in the valley of despair. I say to you today, my friends, so even though we face the difficulties of today and tomorrow, I still have a dream. It is a dream deeply rooted in the American dream. I have a dream that one day this nation will rise up and live out the true meaning of its creed: “We hold these truths to be self-evident: that all men are created equal.” I have a dream that one day on the red hills of Georgia the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood. I have a dream that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice. I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character. I have a dream today. I have a dream that one day, down in Alabama, with its vicious racists, with its governor having his lips dripping with the words of interposition and nullification; one day righ
 fierce urgency of now. This is no time to engage in the luxury of cooling off or to take the tranquilizing drug of gradualism. Now is the time to make real the promises of democracy. Now is the time to rise from the dark and desolate valley of segregation to the sunlit path of racial justice. Now is the time to lift our nation from the quick sands of racial injustice to the solid rock of brotherhood. Now is the time to make justice a reality for all of God’s children. It would be fatal for the nation to overlook the urgency of the moment. This sweltering summer of the Negro’s legitimate discontent will not pass until there is an invigorating autumn of freedom and equality. Nineteen sixty-three is not an end, but a beginning. Those who hope that the Negro needed to blow off steam and will now be content will have a rude awakening if the nation returns to business as usual. There will be neither rest nor tranquility in America until the Negro is granted his citizenship rights. The whirlwinds of revolt will continue to shake the foundations of our nation until the bright day of justice emerges. But there is something that I must say to my people who stand on the warm threshold which leads into the palace of justice. In the process of gaining our rightful place we must not be guilty of wrongful deeds. Let us not seek to satisfy our thirst for freedom by drinking from the cup of bitterness and hatred. We must forever conduct our struggle on the high plane of dignity and discipline. We must not allow our creative protest to degenerate into physical violence. Again and again we must rise to the majestic heights of meeting physical force with soul force. The marvelous new militancy which has engulfed the Negro community must not lead us to a distrust of all white people, for many of our white brothers, as evidenced by their presence here today, have come to realize that their destiny is tied up with our destiny. They have come to realize that their freedom is inextricably bound to our freedom. We cannot walk alone. As we walk, we must make the pledge that we shall always march ahead. We cannot turn back. There are those who are asking the devotees of civil rights, “When will you be satisfied?” We can never be satisfied as long as the Negro is the victim of the unspeakable horrors of police brutality. We can never be satisfied, as long as our bodies, heavy with the fatigue of travel, cannot gain lodging in the motels of the highways and the hotels of the cities. We cannot be satisfied as long as the Negro’s basic mobility is from a smaller ghetto to a larger one. We can never be satisfied as long as our children are stripped of their selfhood and robbed of their dignity by signs stating “For Whites Only”. We cannot be satisfied as long as a Negro in Mississippi cannot vote and a Negro in New York believes he has nothing for which to vote. No, no, we are not satisfied, and we will not be satisfied until justice rolls down like waters and righteousness like a mighty stream. I am not unmindful that some of you have come here out of great trials and tribulations. Some of you have come fresh from narrow jail cells. Some of you have come from areas where your quest for freedom left you battered by the storms of persecution and staggered by the winds of police brutality. You have been the veterans of creative suffering. Continue to work with the faith that unearned suffering is redemptive. Go back to Mississippi, go back to Alabama, go back to South Carolina, go back to Georgia, go back to Louisiana, go back to the slums and ghettos of our northern cities, knowing that somehow this situation can and will be changed. Let us not wallow in the valley of despair. I say to you today, my friends, so even though we face the difficulties of today and tomorrow, I still have a dream. It is a dream deeply rooted in the American dream. I have a dream that one day this nation will rise up and live out the true meaning of its creed: “We hold these truths to be self-evident: that all men are created equal.” I have a dream that one day on the red 
hills of Georgia the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood. I have a dream that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice. I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character. I have a dream today. I have a dream that 
one day, down in Alabama, with its vicious racists, with its governor having his lips dripping with the words of interposition and nullification; one day right there in Alabama, little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers. I have a dream today. I have a dream that one day every valley shall 
be exalted, every hill and mountain shall be made low, the rough places will be made plain, and the crooked places will be made straight, and the glory of the Lord shall be revealed, and all flesh shall see it together. This is our hope. This is the faith that I go back to the South with. With this faith we will be able to hew out of the mountain of despair a stone of hope. With this faith we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood. With this faith we will be able to work together, to pray 
together, to struggle together, to go to jail together, to stand up for freedom together, knowing that we will be free one day. This will be the day when all of God’s children will be able to sing with a new meaning, “My country, ‘tis of thee, sweet land of liberty, of thee I sing. Land where my fathers died, land of the pilgrim’s pride, from every mountainside, let freedom ring.” And if America is to be a great nation this must become true. So let freedom ring from the prodigious hilltops of New Hampshire. Let freedom ring from the mighty mountains of New York. Let freedom ring from the heightening Alleghenies of Pennsylvania! Let freedom ring from the snowcapped Rockies of Colorado! Let freedom ring from the curvaceous slopes of California! But not only that; let freedom ring from Stone Mountain of Georgia! Let freedom ring from Lookout Mountain of Tennessee! Let freedom ring from every hill and molehill of Mississippi. From every mountainside, let freedom ring. And when this happens, when we allow freedom to ring, when we let it ring from every village and every hamlet, from every state and every city, we will be able to speed up that day when all of God’s children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the 
words of the old Negro spiritual, “Free at last! free at last! thank God Almighty, we are free at last!”

Encrypt: 13I0;p4~f5[w8_U8`Z9#j6>D7,s3/t3,r3~T2_w6@n5)s1(p2]q1(K1#l2?w1^q5`K3-i5@V1[i7#x4?I5~J5^W2+m6!a8@a3`U5(T2?k6%N4/n3`f8.K8_m6#d3|z0^U8/V9=R3}P6}C3]N2.M4:q5>j9;I5`W9[i5-M7_u3&e1?X9~F1:Q5(r2:l1?u0@G7/j1}a3`J1:L7|V5{e2{j2@v3;E6.A5/R7{E5$M1$c9=g7:G9@l7&g3=g2?j1/r8>B0;J7;L1/c5=I2$w8*u3,u4{l7)Y9$W4,m1=L7*J2:V0&m2}v2=n8!t4{v5%C5!f4.W2[J7?k6@m0=S6]I3-q1+F1)o6:a9)g7[N8%p4_b3.Q6;s8_C1(J1(f6:v8{D0`F4}d7>H4#x8*Q8*w0=Z0:B4;z8/E2$j6+J3]c8;J0#a8(T6/V8&n6|J1`Y3.Y9_k1^j5^i8%Z0,F9]k3@W1{h3@h8.r8%V7~h4^H9=U2)w5^T2,w1;D9?h8~c7;t3_N2:F5?l8)X0>H8[y6*l0]n1@a3~U1.H0*x8+R8/j5_D6$g1&e8{L7=v7,H3]S4,h5>Y1!t3,l1*o2(P2#h7~J6?c8#c9_w9*N8>K0}h5|Q7`O1^D1#B0+d0:X7>x3~v7~h0^M9$d5!p7!O2}d1(e8$Z3_Z8+C9-F5?M0#G1)m2}I2^s2*E1%s5(I3^Q9~E1&z2+f5/k8}Y4*Y0(x4-Q5}q7!L3#x5?D3`Z6{q2&l5.L1&R5|G8&s7$F3|x0)b2~U6+v3=q2>O0]L9@u0&k2[G3_e4{K4?x6{Y3.s8~Q7]t0]I0)Z4>f4&j4^g5&n8@J4]P9[C9&T8=r5;g6:V7:I5@V5#Q9[G8]u0.e0!b3_S7&c3>r5@m0.U1}f2^o3;o4?N8%n0~n4)w9-w2[g1;r0$g8?b7-Y8?E2;V7~N9.e4*B2~w7*J3`b4/A7;G6@p3,q1}U8!J6@z8$T0]M6#w9)H7]A3/D5+r8~O0*T1$g6(y1]j1_K4$P5+o0^C6{Q3}i9~E9.B1!T0!P9;m9;R8!m7(k3#N4|u2#N0[Y4|g3]O5}b8,q9*H4_t0&d6_T9;H4.F5:I2-t0:G2@P6#Z7~A7.N5*u3>g1}L6|M5/F1!x9/i5)Y4#B1>Q0`o1~Q7|b0%T0]K5`U1*b2|z9:v4}k4#k0(h3^b6$v1-m1{L9!S2|e1,V8>J4/w2]F9,z4#J8|v3^F3[W8,e2,l3`q9^R5(y1:E3^Z5-M7:b8]k5&j4^b8]o6)C8&e2%u8=v4-t7=J0~I1|i6;y7$L7!L7[k5=O7(X0?X7#K9^z3(I7*x8%o7]p8,P5?p7,y0@J4@w5(y5_T0$r4;g2&C1@C4]K7)G4:d6;N5]H7:e1_e3*B3}n1$l3)X6!n4=N0(v7%w8{N9.I4.Q3*m0.y5$w5)s3.s6@l9{U2?K4|C8!w7=A0_C8;C0:T8`B2_v1&b8/o6]t2~y0,J0&Y3>G0]v2~f6;S3-R4-q7|B1?u7/t3!U3#P8$s4{C5&b8^M9=g4`e9)o8?v9[A6/A2!W6$b9^U8$o1#l8{J6~i6;Y0[n4@W8$w3,q8;Q2~e0}L8[w5+Z3_S9`G2;X4[u3=M6)b3#l3>m3!r9=A4@X1/T0`y1_s5{R0]G0#s8/p3)j0|l6;X0;U7+l6!j4=i5}L3}m1:Q0[T5@O6(O1_R3:b5(F9`j3,K5]E6+m1)I2^Y9{a1,z8[h4]P9`u4*E3/F3)k8[P1&c5@T2,m7>e2+k3#D7$w2^u5.Y3@j1[R3;W3$P6=a9|O3.M1`p7!a1~d4?A8=J7[n7+G2/t2]z2>t0+k1.C3`Z0$A0?m9_E2~i2&s9#l8/E1(h9:g5%a5^o8{D9!E3+v6=R1/t4=N5)D7&c0&q2{K3{b0;S2~C8+s6=p8*t0=a0[x5[o5|s9_B9?x0:x2!C1!m5(F6+U4-k9_L6>Q2-k8?k6_T1=t1[D1`H2]z0=P6/A7*N8~w4:x5`r4~e7*O2#l1,p1>v8@O8~H8*p3;M7_F7_o9]w1-E5,Q5]U3?v7}m4;X6:V7@w7/C1+s7*t8&b1:K1-s4)v9(r7#b0{S3#G1@K3!W6-x2?k2:t1!h9~J2)F5>j5#E4.G9{u6;A8(y6%G3|o7(R4]l0_u5*n0?g8)B5:O6,Q4;G7`H1`c3%k1)c8?H1#H9^B5^B4?s4.u9.z8)n6&P4|b2[F8(O3$K7.V8}q9}C1*x7:k2:A9}j5~N2(b7%o7~o6#U1&C5>U6^U6*c3&p3$b3}P3#H6/r5@j5(f2}g3.S4?a2;z8`r2,R8]e0$E5`J5&K5}l7~j8-H7]I0%H3{S0=q7/m6!j9,s0(R9!r5?Y9`z8*v5}g0.u4:r6$y9$i1}Q3+G6{r0[z3@o5_T9;f4{Z4+l4}v5^C4&k3`w8?f5.Z5@R2$t3%Y1~C5$S7{W4{g7=Y8+Z7$a5{E5-a4:Q1*x1)w6%A8[g6{l5/i4@s9/V4`W6;o3@N9~O7)e0?p8.I3*z0&N4^i6}E4>c6;Y1_u1=Z1+u3=X5{C0.I8@X9&V5!i4%c7#V6_z7)S0&g1$X5*z8^i7?S0/x9&u7{O2&Y4+M5|w3/I9&L4)y8*s6-L5&s1^d4?Z9/R8|g9.D9{Z6^X5}z9&N0#I6!a3-C3&s5^c5!P9?O4;w3?f4;u0,m2;d8=z9~V5=H7,u1}F9[B6&u1]P5;b2?N6{o8%I6]n8{d8%D9{T9]X0~z4;M2]p0^K7!a9>N0|K3~Y7-c4>S1|H9.O2;b5{r0*i8:X5:W2%G0!l7(G8,f6$Z4=L1^P8)f2%t9/P8~t4$T1^D7=J7/D3/G7*a4_y6$V0}K0#m1%O0;G8*Q8^r1;v0?W1~C6$V3`b9{a7;N2^h4*j9/y9#R5=p0]U6&r1[S8@S9/F9%J1~U2`Z6/C5+n6%B8(n4-L8!b7,z1~R5^b9)U6,f0+k0%T0&z9{z5$K0/F5{P8#h1*b1;T8_r7>X2/c4;E3+T7&u2_k8#M6^n3}Y7`f1[S7}N9`x9$G7+T0^b0=D8.M7`E7&H8|H0{j3>S6*Q2.Q4[d2;D4]c3?X5@J9:q5{f7(l1;Y9=y6+l2,T9.Q5}S3[b9@G7#b7>I3]B4-T1[n3+Y4?N6^r8]t0}o2,g4?E4>H0-v6,R0_g4`H7+D8.u6}K9*v8^x9^f5$l9(k3`Z2`E3;m1=j1#a1:y2}K0^Q1:n7?P5]p0:K3)K8!h0^h5{s4>o6#h2}E0=o6>A2?U3,x4?I7^e6%y4~i7&t0^X6$Q8:Q2]n3!q1|c9|P2+L3*E3=R6;A3[x3&y3$g7#K9|n8*k1$P8)q8#s5#G8{t5.a9{z9?y8$E9;R5=s7[I8#T4(s7,w6$e5[z4^r7/l9{u1/D9:v6|b4)A3.d7[L9`c1|h7_T7.Z8$i9|M2/K3$M9]f9_F6?U1%h1=G3#l7?A1?B0!R6)Z5}S5;q5_u3_d3`u0&l0}W7#v3@N6[I2%M2&i2}C1!a5#p3?P3_B7_X5+w6=m7#C1]q6~l2]D5.D9]p9!r1-F3%F7]j3+x2@i7=A8)M7=i5-z2]z7*a9!E5/p1{b6/c9$v5.m3~c2*c6#U7(c6=V6:N8+n3$b0:Z9}K6{R5$m1%Z7.o8]o4:S9~L6=n0|B7]g5+N9;y7?n5`Y8}n1`q8@K5}A4?M9$b5@o6*N2^j8,n5@A9_N5)I0-g0~f8+Y7/B8:B1~r8}s8_i9%c8*C6>w8.r3-g0!D2(x9.R9$O1!U3+x6&x4+E9=u5)Y7!V4:O3]M0/I1+W8&c9^L8#m0*G2)J5,v9`c1/k8.P0{V3@B8,T8#e4.v0?o1*v3)q4?U8@Z9.A2#f0.p6&F0~n5-I8^Y4}l6$q9$u4~E3^f2?q3{a8)T4!I7:D2*a4_C2^g6)N7{W0!l1>N0]Y6@D9=x6:f3-e8+b1}y7^K7+x3.y5,G5,s3+W5^N5$r2=W0~V8(b3;y3[i7{t9-E2&u8-m5%R8)l0#z1&V0+U0$r1)g6!e2.h3^l2,m2*U5@W9=Z8(Y8+P0/c5.M6>G4(B3{K7^O0*x4}S3$O1-B9{S0.v0-q2/l2?i0.S1~v4>P5^Q5[B6~y6(Q8:l5/A2,d9.i4=z7&I6-J3&b3]i1}g7^h4]s3*J8+R2_Z2*J3&g2$s6?Q1[X8`q0&c5+q4$f0-V1[r5?K2.U5$c1>i0;r7=Z9+a1:G2^e7|L3&l4(o9&F1-i5^u4~W5*c7;V7>g9/h6}M0)j3|R7+D4:j3,c4/l6}l6-n7!j3@J9.k6&j9#S4`h2;D1,w4>o2@z0`L5.N3!q8,H4)S4)e5}A8_h1%i9)m5{h4{C4[c3}U2*w7`i1*F1#p1%D3`o1]J8{Y9]h1=P5-G3-n7]n1=V6=E5%Y3}o9~e5?X5&X1(I3@k6]d2)i7`U6|r6#c0,B1,m8=E6=j7:j9(i3/f5?i9}R5~s1*D2[C1=S6[R7%m0^m5.K4|a8^y6[R3*q3@f4`V1{N4.X9&V1$N7?z5[Z0&F0$H2)b6;z0?M7:O4=M5|G4~H0+x5{T7*z5`T2.L2@I3}N8]Q4>P5=Q0*Q3]w5`o7{k6{v0.W7:O4~P0)X0]f2^l6:N0+a8]w9>g0_w8[H8&x7.U1-D9+C2*Q3*s1>O5@b8[F2*G8&Y7!a5~M0=C9}T9*t6,N7=O2%B7}X7*g3.g1.n9=T5*x9&V7_Y0[E1@M0+y6.s1#w9=Z2}m3&R4}j0+w4;U9,w3&r1%L9`P6(x4=P5!a3`y6&i4!x0>z4@H7|A5{D6=o0!q2*K8%e3.n8;G9_O7_N6:R5%B7@G0*e6$f8.u3-o3=n8?p7>w0@v2_C1>V4:U9+a0!A5,i6=S2-s8=Q2/M8:y6?h4}A0_c7;a1/g7(N1~h0,Q7:V1#p2^a6^f4@x2$w2-v3=B5!Z7}E5#N9$X0~B0:K6>M4^B0,O1-U4/T0.T4`s0>K6;y7%s1^B4^R1%x9)o4(V1*m8^I3/D1#f6(j2~A9(a6:y4!S5:F1!u8_l7_T3`d0[s6#B8|f0$g7;W5,o7(z9^q5{o9%m2(x4@F8^m0:t2}H9`w8,q7)e9%l6@T5]V5=F0/o8/Z0?t7(a1[T6+k4|T7_u8>u1`y4=w6)j3|c3?o1>V6[D7/q9*v2=D6?C2!g4+Z8=G7/Z9=s9}F4{L5_i8-P6[n3]F6~b0=c9:H6+F2!r3~R4{T2:f6#Y1(Y6-s5,E4=a9|P5?B6*d4>W8:P9^F4#o0|I9#k4>U8+n4_G8!q4#a3?N6:O3;i0]A1%U1#L1>i6|a8~v8_J0;J3+s5,A7+U9{E9!U1#G1)n1{J3]X6$M0@T1+V6@m8`V2[T9~U2}J0%v0>E0~d8:D8`u5&U7]F5:b1(Q6@Q7&h5$z9?W0_I4,c8%u8]s9)y4:J7#h9_B7;o2#f9-W8(c1*a8;X5=D0:Y9&Y3$M3[K6/A1$f3%s8`m3#u1=p9_M6_r8]h1?L7*X8}A7?I2}h2^I6#u8$D5_c0#R1?t1,r6$H2:o0?V8-l2(p9@a0)L8]m4=T5:G2;q4^r7%q7$X6#k0=x8[k2&I1*I9^J0%S3(T3:k1%w1~K9.Z6|i9}L3?R1:g0^O8~F1>q5+Q2?f3^G9@B1|S0{b6.U2=m0=r1(h4}P4^M0|T2;m3+f7@a3=r8!Q4}U4)r5{O5!x2`v2*g4@Y1#p2>e9|W5=T2.H4?h3~l4/i9.i5*X5]T8*l5.J8)i4[T4:z7_m0!k9(x9;g6;i1^c8;j1~l7$X0)r5.q0_L8$y0|K8@Z3)z2|V6!U6&E7{U9.L9*O0{t6*Q1@q7#g5[A6?o1+K7*l4~G6^j7*p2[S7)L8*x3[l5?A3$w5$U8%k6`T5{l7/o0)g3(o3>i7%e8{K8}R8}m9}A9[z2^R8#E0]G6@K7,N1.l2(k1;a5`x1}e2_c0/L0`c3~c1)h9;T5:y2+p5|J3]g2>i8%Q6&C3,P6@W4]c5$f3%k4.E3^j3#o9!r9-W5*H5@b1)k4*I9^z6}D9;V9*b3(m6}w7!z8.d2[H6/S7,o9`k9>i2:T5,Y4@h5]S6`g2#m2_E8;k5}S9%Y5!L9(H1?i2/v9{n4@T4*N0/o1?W0%O9&h1$J8#i9:r3#d8%d8!g5;b8/m6|D5?w0+F8&y5)K2=V6[l2(R7/m7~y7^H2~Q6`y6)p2:f3#l6`S9)L3&o1;f2%E5(x7?N2!f4;U4&i6@W0^H2@F2~X6/c0_r0|H1>v2.A6_j2(z3[i1;C3]p8+S4.P3)Q0{u0?s1#Z6{t5^n7~B1,k8;n1)P9!r7_J9=K8!v8[y5%f1^e3{A1|z9#t6&o1.N0^t1)s0$k4}E7@V0%g5#E9{J4(Y0$j6,p5=i2;M7=Z7!f0^u4.o0`p6[W1}k6}w4^N4|N9%W4|f8~t6`a2]b0~u6^D1#R1,B4_C0`y7&Z8{q8(x6{s6+D0^J3?u9-r0^c7~U6{X5>h4&D2=b8-G3_y5:E3>e4/P4_L6|X0+E1=P4;i3*D9{T4!V4_g2:V5]k6-i1~G2@g6_R6,k4>N2%I2?H3:d1-G6)d8>C9^S3~n4]k6&d5}R7_h6}x8$X7.L3,I1>J5}z2%Z2$J4@z7_V2/K0`t4@s1%D8{R8:q8$J0|p2?u7#G7~p2)N5.I5&S9?v2&e4$U7%p1,w0%s2}l4%k7?H6{u5`Y1^H6*T6/r3!V4)I8/T2%d4+p5?I8|x6+v8$p6-v0/z5?l7&x6}g5;G5[I5*u2=F9.L2.g6^e7/k7`f0?P4|b4|W5@Z7^J6>C3}c2~P5$O9>k9}f2*U1[S5`g8>i4}M7*d0;r7)n7/I9#f5?k2@J6*D3!D7!K5]J2{p2;N0&t4=H0[r9%K0#e6;o1;Q5`o1:e7#N9;Z5[V4-Y2$M7^o6.i2)U0,Z5[I2/D2+u5]L3/D4[N8;U0+k9]Y1`t3%S9)w2^s5}z1`Q5)Z3+B9|F7]X6}F2.T6-R3?S5,Z3(P9+v9=l3.U5,C9_N9]q8#d7_t8)j8|U2]c8%q6&j0|S0)s8[G2[p0%C0:O2[w4=H3~x1[F2=U1{n8_j3]F3~E0-A2$Y8^p0[D5)t8*N7/q2&r6}u2(o5!O4#W8)j4$K0(u8_m4-z7!L0(l1@w1(W6$O4,f7!o4}S1~C4-T9/I5;Q4$F2(c1$i9-l5[C7-r2|l4)l0/X0;J3:R0~F0;p7:f9|l7&Q9{a3=D2{J0#D0}U3/f1&H3_H3$s8(S1)Q9$e1=s2{s6.L9)N8!R2?g5}L7^h7/w9*N9=y1(Z2[N9?w9]t1-E3*p1^Y0?L0{q1^J4!n5*B2%I1^r0+x0>k5`K1%S9,m8_y8)J5{B4!r6|s1~K4#Q9_v5>j6?W6*a0&g6/X5)K7-E8(H1+a1;K4!R5)l8.q1$G8?e0!w0|f3?z6:l1>u5[S3(T3:H8]e7!y5/n8$a7#G4%b9%r8[G0~k4`M1,W1(r7@v2!f9&Q6%l4&n6%N4=u7$M4~A5%G1?o6)H2-q4)T9^L9.Z8|T3@J7>r7.H5`J2!N0`p9:C1}V7[e2?Y4,f3,C5~v1`N8.O2,W8%i7^F3^j9:W3.B1>L4#R9;u6]J8?K9#z7-M9;k8@o9:i1&f9>x0[Z7:L0{b7,J0>F6)W2,u4*H4`r0[s7)j9(w2]I5^k1#g1]s7)U5*A0=N6{G6(y0^s4.y2*H3$z0%f0$k4^q6{x2:I0|Q7+C2(T7,L6+i6&N0=y0*O8,T1+z7^a9,R3?n5$t6.q4&s8!S9%N5:X4>n5#K6-R5%h1*y0,x2#V1/z4]s0)r8:J8-t5>X1]W1#L7)h0;m4+m9~d1/y6$z1*E9]V4_i9`v2#m5^m3(r3,i2?d2)h5!z2&i8`e3:E9}S4/H8_w0)X0}u7#Y5/t4}m9/T1]s6#G3@f4_Z8$m4|k8=N3`M1.B2-Q6/m4?w8)f7_E6?p6.P3(b3&R1+q9:L6$G5)w2%T6(O3#w5@Q3=r2;Z3%F5(D3/x6|g5!y5!o3|C9{t3!S8-f8.c7>c6`F9+C5)V5`Y2]K5$g2?I9&U0{O5=H0:q7}m6>P2.f8@R6.C1#e6`f4}y8%e2:x4{K8|c2~M5=G6`n1%j6[e1(Y0/i7_v0|f1%r4}N3}W0@O9(h7~G9_b0/d4{e4$J2&T4=x5&m2(i4{v4|X5[g6`o1_y5#Y5&k6&Q3_V7=n5-H5?r5$P4]Y5-F5:n4}H3-f4=H2)m9]S8^C1,H5)G8:c1@u2;X9>C6,Q2/n1^f5,D7)s7#s3`s0[t4_i6)I1:C3`g6?N4!r0_L7[B0!U1(M6|K0%p2+H5:M2=o1*f8.l0?t8#F9.b7%r3/A4!w0|B6{T7]I5)M2{V6^Q2$U1=I4|D3~E3)h4=x7^Q1{G1>F0]W3@d8*Q2*O5,Q3,z6(V6@j5*F2~s6`J0]U3~k6~s0.l5|d8_g5?b1.B6.e8&y4?M2-Z8$k5#Q3[M8#E4%D8&b4{H2[G0(J9^k5{X4(p3]w0:X0@C4+n5^s5(u4.F7.E3?D9,f5(K2]G5^f0?J2`W0)r0@Z6$z1[C9>d9!e4#Q7{z4/f2.P4_y0#t1&m4{w0,X4>h3,V3{X9[U8~S6[m6;o7]m9|L5]j7]L4:i3+B6-i3$e7_I4[V7:P4[f6/U8^r1,M7-q4{O5]l7&O7-N3!M2?G4>H0$t4+r8-s0`T7#C9@J1,X0}p7_T8]e8}g1-i2_f4,t8[l7}J0$M0]v1[N3%O4+j

Decrypt: I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in the history of our nation. Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity. But one hundred years later, the Negro still is not free. One hundred years later, the life of the Negro is still sadly crippled by the manacles of segregation and the chains of discrimination. One hundred years later, the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity. One hundred years later, the Negro is still languishing in the corners of American society and finds himself an exile in his own 
land. So we have come here today to dramatize a shameful condition. In a sense we have come to our nation’s capital to cash a check. When the architects of our republic wrote the magnificent words of the Constitution and the Declaration of Independence, they were signing a promissory note to which every American was to fall heir. This note was a promise that all men, yes, black men as well as white men, would be guaranteed the unalienable rights of life, liberty, and the pursuit of happiness. It is obvious today that America has defaulted on this promissory note insofar as her citizens of color are concerned. Instead of honoring this sacred obligation, America has given the Negro people a bad check, a check which has come back marked 
“insufficient funds.” But we refuse to believe that the bank of justice is bankrupt. We refuse to believe that there are insufficient funds in the great vaults of opportunity of this nation. So we have come to cash this check — a check that will give us upon demand the riches of freedom and the security of justice. We have also come to this hallowed spot to remind America of the fierce urgency of now. This is no time to engage in the luxury of cooling off or to take the tranquilizing drug of gradualism. Now is the time to make real the promises of democracy. Now is the time to rise from the dark and desolate valley of segregation to the sunlit path of racial justice. Now is the time to lift our nation from the quick sands of racial injustice to the solid rock of brotherhood. Now is the time to make justice a reality for all of God’s children. It would be fatal for the nation to overlook the urgency of the moment. This sweltering summer of the Negro’s legitimate discontent will not pass until there is an invigorating autumn of freedom and equality. Nineteen sixty-three is not an end, but a beginning. Those who hope that the Negro needed to blow off steam and will now be content will have a rude awakening if the nation returns to business as usual. There will be neither rest nor tranquility in America until the Negro is granted his citizenship rights. The whirlwinds of revolt will continue to shake the foundations of our nation until the bright day of justice emerges. But there is something that I must say to my people who stand on the warm threshold which leads into the palace of justice. In the process of gaining our rightful place we must not be guilty of wrongful deeds. Let us not seek to satisfy our thirst for freedom by drinking from the cup of bitterness and hatred. We must forever conduct our struggle on the high plane of 
dignity and discipline. We must not allow our creative protest to degenerate into physical violence. Again and again we must rise to the majestic heights of meeting physical force with soul force. The marvelous new militancy which has engulfed the Negro community must not lead us to a distrust of all white people, for many of our white brothers, as evidenced by their presence here today, have come to realize that their destiny is tied up with our destiny. They have come to realize that their freedom is inextricably bound to our freedom. We cannot walk 
alone. As we walk, we must make the pledge that we shall always march ahead. We cannot turn back. There are those who are asking the devotees of civil rights, “When will you be satisfied?” We can never be satisfied as long as the Negro is the victim of the unspeakable horrors of police brutality. We can never be satisfied, as long as our bodies, heavy with the fatigue of travel, cannot gain lodging in the motels of the highways and the hotels of the cities. We cannot be satisfied as long as the Negro’s basic mobility is from a smaller ghetto to a larger one. We can never be satisfied as long as our children are stripped of their selfhood and robbed of their dignity by signs stating “For Whites Only”. We cannot be satisfied as long as 
a Negro in Mississippi cannot vote and a Negro in New York believes he has nothing for which to vote. No, no, we are not satisfied, and we will not be satisfied until justice rolls down 
like waters and righteousness like a mighty stream. I am not unmindful that some of you have come here out of great trials and tribulations. Some of you have come fresh from narrow jail 
cells. Some of you have come from areas where your quest for freedom left you battered by the storms of persecution and staggered by the winds of police brutality. You have been the veterans of creative suffering. Continue to work with the faith that unearned suffering is redemptive. Go back to Mississippi, go back to Alabama, go back to South Carolina, go back to Georgia, go back to Louisiana, go back to the slums and ghettos of our northern cities, knowing that somehow this situation can and will be changed. Let us not wallow in the valley of despair. I say to you today, my friends, so even though we face the difficulties of today and tomorrow, I still have a dream. It is a dream deeply rooted in the American dream. I have a dream that one day this nation will rise up and live out the true meaning of its creed: “We hold these truths to be self-evident: that all men are created equal.” I have a dream that one day on the red hills of Georgia the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood. I have a dream that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice. I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character. I have a dream today. I have a dream that one day, down in Alabama, with its vicious racists, with its governor having his lips dripping with the words of interposition and nullification; one day right there in Alabama, little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers. I have a dream today. I have a dream that one day every valley shall be exalted, every hill and mountain shall be made low, the rough places will be made plain, and the crooked places will be made straight, and the glory of the Lord shall be revealed, and all flesh shall see it together. This is our hope. This is the faith that I go back to the South with. With this faith we will be able to hew out of the mountain of despair a stone of hope. With this faith we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood. With this faith we will be able to work together, to pray together, to struggle together, to go to jail together, to stand up for freedom together, knowing that we will be free one day. This will be the day when all of God’s children will be able to sing with a new meaning, “My country, ‘tis of thee, sweet land of liberty, of thee I sing. Land where my fathers died, land of the pilgrim’s pride, from every mountainside, let freedom ring.” And if America is to be a great nation this must become true. So let freedom ring from the prodigious hilltops of New Hampshire. Let freedom ring from the mighty mountains of New York. Let freedom ring from the heightening Alleghenies of Pennsylvania! Let freedom ring from the snowcapped Rockies of Colorado! Let freedom ring from the curvaceous slopes of California! But not only that; let freedom ring from Stone Mountain of Georgia! Let freedom ring from Lookout Mountain of Tennessee! Let freedom ring from every hill and molehill of Mississippi. From every mountainside, let freedom ring. And when this happens, when we allow freedom to ring, when we let it ring from every village and every hamlet, from every state 
and every city, we will be able to speed up that day when all of God’s children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the words of the old Negro spiritual, “Free at last! free at last! thank God Almighty, we are free at last!”
```
