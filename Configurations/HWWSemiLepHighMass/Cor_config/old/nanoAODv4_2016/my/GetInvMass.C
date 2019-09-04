#include "TLorentzVector.h"
float GetInvMass(float pt1,
	    float eta1,
	    float phi1,
	    float m1,
	    float pt2,
	    float eta2,
	    float phi2,
	    float m2){


  TLorentzVector v1,v2;
  v1.SetPtEtaPhiM(pt1,eta1,phi1,m1);
  v2.SetPtEtaPhiM(pt2,eta2,phi2,m2);
  
  float M=(v1+v2).M();

  return M;



}
