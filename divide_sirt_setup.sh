#!/usr/bin/env bash

mkdir phosphorus/sirt
clip divide -mode 2 phosphorus/P-a_ali.mrc phosphorus/P-b_ali.mrc phosphorus/sirt/P-divide_ali.mrc
cp phosphorus/tiltb.com phosphorus/sirt/tilt-divide.com
cp phosphorus/P-b.tlt phosphorus/sirt/P-divide.tlt
cp phosphorus/P-b.xtilt phosphorus/sirt/P-divide.xtilt
sed -i com 's/-b/-divide/g' phosphorus/sirt/tilt-divide.com

cd phosphorus/sirt
sirtsetup -nu 8 -it 15 -st -le 5,10 tilt-divide.com
cd ../..

mkdir nitrogen/sirt
clip divide -mode 2 nitrogen/N-a_ali.mrc nitrogen/N-b_ali.mrc nitrogen/sirt/N-divide_ali.mrc
cp nitrogen/tiltb.com nitrogen/sirt/tilt-divide.com
cp nitrogen/N-b.tlt nitrogen/sirt/N-divide.tlt
cp nitrogen/N-b.xtilt nitrogen/sirt/N-divide.xtilt
sed -i com 's/-b/-divide/g' nitrogen/sirt/tilt-divide.com

cd nitrogen/sirt
sirtsetup -nu 8 -it 15 -st -le 5,10 tilt-divide.com
cd ../..

