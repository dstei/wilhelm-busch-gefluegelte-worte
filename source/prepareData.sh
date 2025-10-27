./mysplit < de_head_0000_2020-10.txt > de_head_0000_2020-10_lines.txt
split -C 800m --numeric-suffixes de_head_0007_2020-10_lines.txt de_head_0007_2020-10_
sed -i '1d' de_head_000{5,6,7}_2020-10_00
