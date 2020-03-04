#include <TFile.h>
#include <iostream>
#include <TLorentzVector.h>
#include <TTree.h>




namespace multidraw {

  extern thread_local TTree* currentTree;

}




float CleanJet_pt[20];
float CleanJet_eta[20];
float CleanJet_phi[20];
int CleanJet_jetIdx[20];
UInt_t nCleanJet;
float Jet_mass[30];
float MW=80.4;


//UInt_t

//---variables
float Lepton_pt[10];
float Lepton_eta[10];
float Lepton_phi[10];
float MET_pt;
float MET_phi;

//float PuppiMET_pt;
//float PuppiMET_phi;

TLorentzVector Wlep,Whad;
float sol1, sol2, met_pz_1, met_pz_2;


float VBF_jjdEta;
float VBF_Mjj;

int cjidx;

int whad_cjidx1;
int whad_cjidx2;

bool isWhadEvent=false;
bool isVBFEvent=false;


//--To prevent memory leakage
//bool initialized = false;
//TString name_temp = "";



//----1) Make Wlep 



void init_WlepMaker(TTree* tree, TString METtype){

  //tree->ResetBranchAddresses();
  tree->SetBranchAddress("Lepton_pt", &Lepton_pt);
  tree->SetBranchAddress("Lepton_eta", &Lepton_eta);
  tree->SetBranchAddress("Lepton_phi", &Lepton_phi);
  tree->SetBranchAddress(METtype+"MET_pt", &MET_pt);
  tree->SetBranchAddress(METtype+"MET_phi", &MET_phi);

}

int entry_SetWlep=-999;
TString f_SetWlep="";
void SetWlep(int entry,TString METtype){

  if( (f_SetWlep != multidraw::currentTree->GetCurrentFile()->GetName()) ){//if function's file != current file
    init_WlepMaker(multidraw::currentTree, METtype);     //update address of variables   
  }
  
  else if( entry_SetWlep == entry ){ //if both file and entry are already set 
    return;
  }


  // Wlep variables are not set for this event

  f_SetWlep = multidraw::currentTree->GetCurrentFile()->GetName(); // current file
  entry_SetWlep = entry;



  //cout<<"start WlepMaker"<<endl;
  multidraw::currentTree->GetEntry(entry);

  //--Set W mass--//
  float wmass=80.4;
  //--Get the momentum of objects--//
  float lep_pt  = Lepton_pt[0];
  float lep_phi = Lepton_phi[0];
  float lep_eta = Lepton_eta[0];
  float lep_pz  = lep_pt*sinh(lep_eta);
  float lep_E   = lep_pt*cosh(lep_eta);
  float met_pt  = MET_pt;
  float met_phi = MET_phi;

  //met_pz solution = met_pz_1 +-sqrt(met_pz_2)
  float mu       = (wmass*wmass)/2 + lep_pt*met_pt*cos(met_phi-lep_phi);
  met_pz_1 = mu*lep_pz/pow(lep_pt,2);
  met_pz_2 = pow( mu*lep_pz/(lep_pt*lep_pt), 2 ) - ( pow(lep_E*met_pt, 2) - mu*mu )/pow(lep_pt,2);


  //--Let's get the neutrino's pz
  float met_pz=0;
  //1) complex -> Get only real part
  if (met_pz_2 < 0) met_pz = met_pz_1;
  //2) real solution
  else{
    sol1 = met_pz_1+sqrt(met_pz_2);
    sol2 = met_pz_1-sqrt(met_pz_2);
    if(fabs(sol1) < fabs(sol2)){
      met_pz = sol1;
    }
    else{
      met_pz = sol2;
    }
  }

  float wlep_px = lep_pt*cos(lep_phi) + met_pt*cos(met_phi);
  float wlep_py = lep_pt*sin(lep_phi) + met_pt*sin(met_phi);
  float wlep_pz = lep_pz + met_pz;
  float wlep_E  = lep_E  + sqrt(pow(met_pz,2) + pow(met_pt,2));

  Wlep.SetPxPyPzE(wlep_px, wlep_py, wlep_pz, wlep_E);
}


//---Return Puppi
float WlepPuppi_pt(int entry){  SetWlep(entry,"Puppi"); return Wlep.Pt();}
float WlepPuppi_mass(int entry){  SetWlep(entry,"Puppi"); return Wlep.M();}
float WlepPuppi_eta(int entry){  SetWlep(entry,"Puppi"); return Wlep.Eta();}
float WlepPuppi_phi(int entry){  SetWlep(entry,"Puppi");  return Wlep.Phi();}
float WlepPuppi_met_pz_1(int entry){  SetWlep(entry,"Puppi"); return met_pz_1;}
float WlepPuppi_met_pz_2(int entry){  SetWlep(entry,"Puppi"); return met_pz_2;}

//--Return PF

float WlepPF_pt(int entry){  SetWlep(entry,"PF");    return Wlep.Pt(); }
float WlepPF_mass(int entry){  SetWlep(entry,"PF");  return Wlep.M();  }
float WlepPF_eta(int entry){  SetWlep(entry,"PF");   return Wlep.Eta();}
float WlepPF_phi(int entry){  SetWlep(entry,"PF");   return Wlep.Phi();}
float WlepPF_met_pz_1(int entry){  SetWlep(entry,"PF"); return met_pz_1;}
float WlepPF_met_pz_2(int entry){  SetWlep(entry,"PF"); return met_pz_2;}


//----2) Make Whad

void init_WhadMaker(TTree* tree){ // Need Cleanjet kinematics //

  //tree->ResetBranchAddresses();
  tree->SetBranchAddress("nCleanJet", &nCleanJet);
  tree->SetBranchAddress("CleanJet_pt", &CleanJet_pt);
  tree->SetBranchAddress("CleanJet_eta", &CleanJet_eta);
  tree->SetBranchAddress("CleanJet_phi", &CleanJet_phi);
  tree->SetBranchAddress("CleanJet_jetIdx", &CleanJet_jetIdx);
  tree->SetBranchAddress("Jet_mass", &Jet_mass);
  //CleanJet_jetIdx

}



//To prevent double call
int entry_SetWhad=-999;
TString f_SetWhad="";


bool SetWhad(int entry){

  if( (f_SetWhad != multidraw::currentTree->GetCurrentFile()->GetName()) ){
    init_WhadMaker(multidraw::currentTree);  
  }
  else if( entry_SetWhad == entry ){ //if both file and entry are already set
    return isWhadEvent;
  }

  f_SetWhad = multidraw::currentTree->GetCurrentFile()->GetName(); // current file
  entry_SetWhad= entry;


  multidraw::currentTree->GetEntry(entry);



  whad_cjidx1=-1;
  whad_cjidx2=-1;


  int Njet=nCleanJet;
  float dM=99999.0;

    
  for(int ci = 0; ci < Njet; ci++ ){
    //--momentum of 1st jet
    float pt1 = CleanJet_pt[ci];
    if(pt1<30){
      continue;
    }
    float eta1 = CleanJet_eta[ci];
    if(eta1>2.5){
      continue;
    }
    float phi1 = CleanJet_phi[ci];
    float mass1 = Jet_mass[CleanJet_jetIdx[ci]];


    for(int cj = 0; cj < Njet; cj++){
      if(ci>=cj)continue;
      float pt2 = CleanJet_pt[cj];
      if(pt2<30) continue;
      float eta2 = CleanJet_eta[cj];
      if(eta2>2.5) continue;
      float phi2 = CleanJet_phi[cj];
      float mass2 = Jet_mass[CleanJet_jetIdx[cj]];



      TLorentzVector v1,v2;
      v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1);
      v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2);


      
      float this_dM  = fabs((v1+v2).M() - MW);
      isWhadEvent=true;


      //---Compare dM

      if(this_dM < dM ){//if current dM is smaller than previous dM
	//select this jet pair to Whadronic
	dM=this_dM;
	whad_cjidx1=ci;
	whad_cjidx2=cj;
	Whad=v1+v2;
      }


    }
  }
  

  return isWhadEvent;
}


float Whad_pt(int entry){  SetWhad(entry);  return Whad.Pt();}
float Whad_eta(int entry){  SetWhad(entry); return Whad.Eta();}
float Whad_phi(int entry){  SetWhad(entry);return Whad.Phi();}
float Whad_mass(int entry){  SetWhad(entry); return Whad.M();}
float Get_cjidx1(int entry){ SetWhad(entry); return whad_cjidx1; }
float Get_cjidx2(int entry){ SetWhad(entry); return whad_cjidx2; }


//---4)VBF selection
void init_VBF(TTree* tree){

  //tree->ResetBranchAddresses();
  tree->SetBranchAddress("CleanJet_pt", &CleanJet_pt);
  tree->SetBranchAddress("CleanJet_eta", &CleanJet_eta);
  tree->SetBranchAddress("CleanJet_phi", &CleanJet_phi);
  tree->SetBranchAddress("CleanJet_jetIdx", &CleanJet_jetIdx);
  tree->SetBranchAddress("Jet_mass", &Jet_mass);


}


int entry_SetVBF=-999;
TString f_SetVBF="";


bool SetVBF(int entry){

  if( (f_SetVBF != multidraw::currentTree->GetCurrentFile()->GetName()) ){
    init_VBF(multidraw::currentTree);
  }

  else if( entry_SetVBF == entry ){ //if both file and entry are already set
    return isVBFEvent;
  }


  // VBF variables are not set for this event
  f_SetVBF = multidraw::currentTree->GetCurrentFile()->GetName(); // current file
  entry_SetVBF= entry;

  multidraw::currentTree->GetEntry(entry);

  SetWhad(entry); //---to get whad_cjidx1, whad_cjidx2

  VBF_jjdEta = -9999.;
  VBF_Mjj  = -9999.;

  int Njet=nCleanJet;
  for(int ci = 0; ci < Njet; ci++ ){
    if(ci==whad_cjidx1) continue; // first jet is not Whad
    if(ci==whad_cjidx2) continue;
    //--momentum of 1st jet
    float pt1 = CleanJet_pt[ci];
    if(pt1<30){
      continue;
    }
    float eta1 = CleanJet_eta[ci];
    if(eta1 > 4.7) continue;
    float phi1 = CleanJet_phi[ci];
    float mass1 = Jet_mass[CleanJet_jetIdx[ci]];


    for(int cj = 0; cj < Njet; cj++){
      if(ci>=cj)continue;
      if(cj==whad_cjidx1) continue; //second jet is not Whad
      if(cj==whad_cjidx2) continue;
      float pt2 = CleanJet_pt[cj];
      if(pt2<30) continue;
      float eta2 = CleanJet_eta[cj];
      if(eta2 > 4.7) continue;
      float phi2 = CleanJet_phi[cj];
      float mass2 = Jet_mass[CleanJet_jetIdx[cj]];



      TLorentzVector v1,v2;
      v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1);
      v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2);


      float this_dEta = fabs(eta1-eta2);
      float this_Mjj  = (v1+v2).M();

      if(this_Mjj < 500 ) continue;
      if(this_dEta < 3.5 ) continue;
      if(this_dEta > VBF_jjdEta){
        VBF_jjdEta=this_dEta;
        VBF_Mjj=this_Mjj;
      }

    }
  }
  if(VBF_jjdEta < 3.5){
    isVBFEvent=false;
    return false;
  }
  isVBFEvent=true;

  return true;

}


float Get_VBF_jjdEta(int entry){ 
  SetVBF(entry);  
  if(!isVBFEvent){
    return -9999;
  }
  else{
    return VBF_jjdEta;
  }

}


float Get_VBF_Mjj(int entry){
  SetVBF(entry);
  if(!isVBFEvent){
    return -9999;
  }
  else{
    return VBF_Mjj;
  }
}




/*

void init_BJet(TTree* tree){

  //tree->ResetBranchAddresses();
  tree->SetBranchAddress("CleanJet_pt", &CleanJet_pt);
  tree->SetBranchAddress("CleanJet_eta", &CleanJet_eta);
  tree->SetBranchAddress("CleanJet_phi", &CleanJet_phi);
  tree->SetBranchAddress("CleanJet_jetIdx", &CleanJet_jetIdx);
  tree->SetBranchAddress("CleanJetNotFat_jetIdx", &CleanJetNotFat_jetIdx);
  tree->SetBranchAddress("nCleanJetNotFat", &nCleanJetNotFat);
  tree->SetBranchAddress("Jet_mass", &Jet_mass);


}

int entry_SetVBF=-999;
TString f_SetVBF="";


bool SetBJet(int entry){

*/
