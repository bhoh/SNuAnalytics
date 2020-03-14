#include <TLorentzVector.h>
float GetMt(float pt1, float phi1, float m1, float pt2, float phi2, float m2 ){ 
  TLorentzVector v1;
  v1.SetPtEtaPhiM(pt1,0,phi1,m1);
  TLorentzVector v2;
  v2.SetPtEtaPhiM(pt2,0,phi2,m2);

  return (v1+v2).Mt();
}
