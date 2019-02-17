# EncodeDecode
Simple Python script to encode and decode any string.

**The encoding process is:**\
for every charater in the input string,\
replace the character with (`seed_letter`, `seed_number`, `seed_symbol`) combined.\
*i.e., replace the chartater with (one random letter + one random number + one random symbol).*\
then using the same encode method to encode the `seed_combine` that replaced the charater,\
finally we concatenate the two output together and return as one code.\
*Currently the major disadvantage of this encoding method is the output code being too long.*

**The decoding process is:**\
separate the input string as two part: encoded seed, encoded string,\
first decode the seed by matching index of `seed_letter`, `seed_number`, `seed_symbol`.\
then using the seed we can put back each of the replaced character.

### Example runs:
```
Enter: 1
Encode: 645y1}j6)k0.b0%z5>i4?94y1}95j6)94k0.155b0%99z5>82i4?!70n6%
Decode: 1

Enter: 1
Encode: 663p8_o4%w6*x6*u1^i9>112p8_115o4%113w6*174x6*115u1^105i9>!91o4*
Decode: 1

Enter: 1
Encode: 618x8$e8?g8;b5_l5:v6>67x8$73e8?68g8;123b5_67l5:60v6>!121i1*
Decode: 1

Enter: Hello
Encode: e1892j4:t8,z7>e5$w0)e5|y8}p5]j6;w6-n9,f9(f4_y4@v3~r3)s2%n7]145j4:143t8,148z7>210e5$144w0)183e5|201y8}141p5]135j6;203w6-145n9,153f9(197f4_143y4@153v3~201r3)149s2%185n7]!110v4[139m1+146o5=146i3=149m9]
Decode: Hello

Enter: 你好
Encode: 992e2?h3&x4-g1<s1=c7*n4,o4@n8`142e2?143h3&149x4-208g1<146s1=186c7*207n4,145o4@156n8`!20359t6^22948s5@
Decode: 你好

Enter: こんにちは
Encode: m1881g4}y0+m5{k3(x3=r8,g5&d1=z9_f1-o2%w6)h7#p6/n8-q7+e9>e0>134g4}136y0+132m5{192k3(137x3=175r8,183g5&136d1=122z9_197f1-131o2%177w6)202h7#130p6/117n8-202q7+130e9>144e0>!12444o8^12508f7)12468t2`12458y1$12472y1?
Decode: こんにちは

Enter: γεια σας
Encode: k2752t0%b5+h9{r9:h4[r9?h4-m9/u9-a0-h8~o8%a1-s9_c8{y0~a5#p4>m0%i9_j7)s9.a4|y0>a6#p0@m7^108t0%109b5+106h9{159r9:104h4[147r9?154h4-106m9/148u9-161a0-102h8~116o8%173a1-108s9_97c8{161y0~102a5#148p4>154m0%100i9_177j7)167s9.109a4|115y0>164a6#106p0@99m7^!1043k4_1045f6`1049m2@1041y8-128m2`1059f0}1041s9?1058p6/
Decode: γεια σας

```
