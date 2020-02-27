#include <TLorentzVector.h>
#include <iostream>

using namespace std;
float GetMt(float pt1, float phi1, float m1, float pt2, float phi2, float m2 ){ 
  TLorentzVector v1;
  v1.SetPtEtaPhiM(pt1,0,phi1,m1);
  TLorentzVector v2;
  v2.SetPtEtaPhiM(pt2,0,phi2,m2);
  //std::cout <<"v1.Px()="<<v1.Px()<<" v1.Py()="<<v1.Py()<<std::endl;
  //std::cout <<"v2.Px()="<<v2.Px()<<" v2.Py()="<<v2.Py()<<std::endl;
  //std::cout <<"sqrt( (v1.Px()+v2.Px())*(v1.Px()+v2.Px()) + (v1.Py()+v2.Py()*(v1.Py()+v2.Py())))="<<(v1.Px()+v2.Px())*(v1.Px()+v2.Px()) + (v1.Py()+v2.Py()*(v1.Py()+v2.Py()))<<std::endl;
  //std::cout <<"(v1+v2).E()="<<(v1+v2).E()<<std::endl;
  //std::cout <<"(v1+v2).M()="<<(v1+v2).M()<<std::endl;
  //std::cout <<"(v1+v2).Px()="<<(v1+v2).Px()<<std::endl;
  //std::cout <<"(v1+v2).Py()="<<(v1+v2).Py()<<std::endl;
  //std::cout <<"(v1+v2).Pz()="<<(v1+v2).Pz()<<std::endl;

  return (v1+v2).Mt();
}



TLorentzVector _Vdummy;

void Combine2PtEtaPhiM(float pt1, float eta1, float phi1, float mass1, float pt2, float eta2, float phi2, float mass2){
  TLorentzVector v1,v2;
  v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1);
  v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2);
  _Vdummy=v1+v2;
}

float Combine2PtEtaPhiM_Mt(float pt1, float eta1, float phi1, float mass1, float pt2, float eta2, float phi2, float mass2){
  Combine2PtEtaPhiM(pt1, eta1, phi1, mass1, pt2, eta2, phi2, mass2);
  return _Vdummy.Mt();
}

float Combine2PtEtaPhiM_M(float pt1, float eta1, float phi1, float mass1, float pt2, float eta2, float phi2, float mass2){
  Combine2PtEtaPhiM(pt1, eta1, phi1, mass1, pt2, eta2, phi2, mass2);
  return _Vdummy.M();
}

float Combine2PtEtaPhiM_Pt(float pt1, float eta1, float phi1, float mass1, float pt2, float eta2, float phi2, float mass2){
  Combine2PtEtaPhiM(pt1, eta1, phi1, mass1, pt2, eta2, phi2, mass2);
  return _Vdummy.Pt();
}

float Combine2PtEtaPhiM_Eta(float pt1, float eta1, float phi1, float mass1, float pt2, float eta2, float phi2, float mass2){
  Combine2PtEtaPhiM(pt1, eta1, phi1, mass1, pt2, eta2, phi2, mass2);
  return _Vdummy.Eta();
}


float Combine2PtEtaPhiM_Phi(float pt1, float eta1, float phi1, float mass1, float pt2, float eta2, float phi2, float mass2){
  Combine2PtEtaPhiM(pt1, eta1, phi1, mass1, pt2, eta2, phi2, mass2);
  return _Vdummy.Phi();
}
