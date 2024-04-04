echo "copying boundary model from P-b to others..."
cp phosphorus/tomopitchb.mod phosphorus/tomopitcha.mod
cp phosphorus/tomopitchb.mod nitrogen/tomopitcha.mod
cp phosphorus/tomopitchb.mod nitrogen/tomopitchb.mod

echo "copying fiducials from P-b.fid to others..."
cp phosphorus/P-b.fid phosphorus/P-a.fid
cp phosphorus/P-b.fid nitrogen/N-a.fid
cp phosphorus/P-b.fid nitrogen/N-b.fid

echo "Done."
