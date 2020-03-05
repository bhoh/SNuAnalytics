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
