//root -b -l
//gSystem->Load("libLatinoAnalysisMultiDraw.so")
#include <TFile.h>
#include <iostream>
#include <TLorentzVector.h>
#include <TTree.h>




//    'expr':'PrimaryFatJet_cjidx(Entry$,'+maxtau21+','+min_jetId+','+max_jetId+')',

namespace multidraw {

  extern thread_local TTree* currentTree;

}
UInt_t nCleanFatJet;

float CleanFatJet_pt[10];
float CleanFatJet_eta[10];
float CleanFatJet_phi[10];
float CleanFatJet_mass[10];
float CleanFatJet_tau21[10];
int CleanFatJet_jetIdx[10];

int FatJet_jetId[10];

float CleanJet_pt[20];
float CleanJet_eta[20];
float CleanJet_phi[20];
float CleanJet_jetIdx[20];



UInt_t nCleanJetNotFat;
int CleanJetNotFat_jetIdx[20];

float Jet_mass[30];



//UInt_t

//---variables
float Lepton_pt[10];
float Lepton_eta[10];
float Lepton_phi[10];
float MET_pt;
float MET_phi;

//float PuppiMET_pt;
//float PuppiMET_phi;

TLorentzVector Wlep,WWFat;
float sol1, sol2, met_pz_1, met_pz_2;


float VBF_jjdEta;
float VBF_Mjj;

int cjidx;

bool isFatJetEvent=false;
bool isVBFEvent=false;

//--To prevent memory leakage
//bool initialized = false;
//TString name_temp = "";



//1)----- FatJet Selector----//
void init_FindPrimaryFatJet(TTree* tree){
  //tree->ResetBranchAddresses();
  tree->SetBranchAddress("nCleanFatJet", &nCleanFatJet);
  tree->SetBranchAddress("CleanFatJet_pt", &CleanFatJet_pt);
  tree->SetBranchAddress("CleanFatJet_mass", &CleanFatJet_mass);
  tree->SetBranchAddress("CleanFatJet_eta", &CleanFatJet_eta);
  tree->SetBranchAddress("CleanFatJet_phi", &CleanFatJet_phi);
  tree->SetBranchAddress("CleanFatJet_tau21", &CleanFatJet_tau21);
  tree->SetBranchAddress("CleanFatJet_jetIdx", &CleanFatJet_jetIdx);
  tree->SetBranchAddress("FatJet_jetId", &FatJet_jetId);

}

int entry_FindPrimaryFatJet=-999;
TString f_FindPrimaryFatJet="";



bool FindPrimaryFatJet(int entry, float maxtau21, int min_jetId, int max_jetId){


  if( (f_FindPrimaryFatJet != multidraw::currentTree->GetCurrentFile()->GetName()) ){//If this function's file is not matched to current file
    init_FindPrimaryFatJet(multidraw::currentTree);  //Need to update branch address to current one
  }

  else if( entry_FindPrimaryFatJet == entry ){ //if both file and entry are already set -> This PrimaryFatJet selection was called before.
    //No need to be recalled
    return isFatJetEvent; //
  }


  //update function's file to current one
  f_FindPrimaryFatJet=multidraw::currentTree->GetCurrentFile()->GetName();
  //update function's entry to current one
  entry_FindPrimaryFatJet=entry;

  multidraw::currentTree->GetEntry(entry); //read current entry
  //int nCleanFatJet = CleanFatJet_pt.size();

  float pt_prifat = 200; // minimum pt for fatjet and last selected fatjet's pt
  
  cjidx=-1;
  for(unsigned int i=0; i < nCleanFatJet; i++){
    float tau21 = CleanFatJet_tau21[i];
    float pt    = CleanFatJet_pt[i];
    float jetId = FatJet_jetId[CleanFatJet_jetIdx[i]];
    float mass = CleanFatJet_mass[i];
    float eta = CleanFatJet_eta[i];
    if (mass < 40 ) continue; // include SB / SR
    if (mass > 250 ) continue;// include SB / SR
    if( tau21 > maxtau21 ) continue; //tau21 maxcut
    if (fabs(eta) > 2.4 ) continue;
    if(pt < pt_prifat) continue; //if pt < 200 OR pt(lastest selection FatJet)
    //Not energetic enough, continue
    if(jetId<min_jetId) continue;
    if(jetId>max_jetId) continue;

    //if passsed all cuts, this fatjet is the primary fatjet now.
    pt_prifat=pt; //update pt_prifat to current fatjet

    cjidx=i; //passed all criteria -> Primary fatjet. cjidx : cleanfatjet index of primary fatjet
  }
  
  //std::cout << "cjidx=>" << cjidx<<std::endl;

  if(cjidx<0){// if there's no FatJet pass all cuts cjidx is not updated -> cjidx==-1
    isFatJetEvent=false;
    return false;
  }
  //if not returned, there's a Fatjet passing the selection.(FatJetEvent)
  isFatJetEvent=true;
  return true;

}



float WFatJet_pt(int entry,float maxtau21, int min_jetId, int max_jetId){//Primary FatJet's pt
  FindPrimaryFatJet(entry,maxtau21,min_jetId,max_jetId);
  if(cjidx<0){
    return -999.;}
  
  return CleanFatJet_pt[cjidx];
}


float WFatJet_eta(int entry,float maxtau21, int min_jetId, int max_jetId){
  FindPrimaryFatJet(entry,maxtau21,min_jetId,max_jetId);
  if(cjidx<0){
    return -999.;}
  
  return CleanFatJet_eta[cjidx];
}

float WFatJet_phi(int entry,float maxtau21, int min_jetId, int max_jetId){
  FindPrimaryFatJet(entry,maxtau21,min_jetId,max_jetId);
  if(cjidx<0){
    return -999.;}
  
  return CleanFatJet_phi[cjidx];
}

float WFatJet_mass(int entry,float maxtau21, int min_jetId, int max_jetId){
  FindPrimaryFatJet(entry,maxtau21,min_jetId,max_jetId);
  if(cjidx<0){
    return -999.;}
  
  return CleanFatJet_mass[cjidx];
}


float WFatJet_tau21(int entry,float maxtau21, int min_jetId, int max_jetId){
  FindPrimaryFatJet(entry,maxtau21,min_jetId,max_jetId);
  if(cjidx<0){
    return -999.;}
  
  return CleanFatJet_tau21[cjidx];
}


//----2) Make Wlep 

void init_WlepMaker(TTree* tree, TString METtype){

  //tree->ResetBranchAddresses();
  tree->SetBranchAddress("Lepton_pt", &Lepton_pt); //need lepton's momentum
  tree->SetBranchAddress("Lepton_eta", &Lepton_eta);
  tree->SetBranchAddress("Lepton_phi", &Lepton_phi);
  tree->SetBranchAddress(METtype+"MET_pt", &MET_pt); //need MET pt and phi-direction
  tree->SetBranchAddress(METtype+"MET_phi", &MET_phi);

}


int entry_SetWlep=-999;//entry # of function
TString f_SetWlep="";  // file name of function


void SetWlep(int entry,TString METtype){

  if( (f_SetWlep != multidraw::currentTree->GetCurrentFile()->GetName()) ){//if function's file is not match to current file 
    init_WlepMaker(multidraw::currentTree, METtype);  //update address to current one
  }
  else if( entry_SetWlep == entry ){ //if both file and entry are already matched->this function has been called before for this event
    return;
  }

  f_SetWlep = multidraw::currentTree->GetCurrentFile()->GetName(); //Set function's file to current one 
  entry_SetWlep= entry; //entry of this function = current entry

  multidraw::currentTree->GetEntry(entry); //Get entry

  //--Set W mass--//
  float wmass=80.4;
  //--Get the momentum of objects--//
  float lep_pt  = Lepton_pt[0]; //primary lepton's pt //need to update order of lepton ????
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
    if(fabs(sol1) < fabs(sol2)){ //choose one with smaller abs value
      met_pz = sol1;
    }
    else{
      met_pz = sol2;
    }
  }
  //Now neutrino momentum is reco.

  float wlep_px = lep_pt*cos(lep_phi) + met_pt*cos(met_phi);
  float wlep_py = lep_pt*sin(lep_phi) + met_pt*sin(met_phi);
  float wlep_pz = lep_pz + met_pz;
  float wlep_E  = lep_E  + sqrt(pow(met_pz,2) + pow(met_pt,2)); //massless particle

  Wlep.SetPxPyPzE(wlep_px, wlep_py, wlep_pz, wlep_E);
}


//---Return Puppi
float WlepPuppi_pt(int entry){  SetWlep(entry,"Puppi"); return Wlep.Pt();}
float WlepPuppi_mass(int entry){  SetWlep(entry,"Puppi"); return Wlep.M();}
float WlepPuppi_eta(int entry){  SetWlep(entry,"Puppi");return Wlep.Eta();}
float WlepPuppi_phi(int entry){  SetWlep(entry,"Puppi"); return Wlep.Phi();}
float WlepPuppi_met_pz_1(int entry){  SetWlep(entry,"Puppi"); return met_pz_1;}
float WlepPuppi_met_pz_2(int entry){  SetWlep(entry,"Puppi"); return met_pz_2;}

//--Return PF
float WlepPF_pt(int entry){SetWlep(entry,"PF");return Wlep.Pt();}
float WlepPF_mass(int entry){  SetWlep(entry,"PF");return Wlep.M();}
float WlepPF_eta(int entry){  SetWlep(entry,"PF");  return Wlep.Eta();}
float WlepPF_phi(int entry){  SetWlep(entry,"PF");  return Wlep.Phi();}
float WlepPF_met_pz_1(int entry){  SetWlep(entry,"PF");  return met_pz_1;}
float WlepPF_met_pz_2(int entry){  SetWlep(entry,"PF");  return met_pz_2;}


//---4)VBF selection
void init_VBF(TTree* tree){

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

bool SetVBF(int entry){

  if( (f_SetVBF != multidraw::currentTree->GetCurrentFile()->GetName()) ){
    init_VBF(multidraw::currentTree);  
  }
  else if( entry_SetVBF == entry ){ //if both file and entry are already set
    return isVBFEvent;
  }

  f_SetVBF = multidraw::currentTree->GetCurrentFile()->GetName();
  entry_SetVBF= entry;

  multidraw::currentTree->GetEntry(entry);

  ///if # of addtional jet is less than 2 -> cannot make a forward pair 
  if(nCleanJetNotFat<2){
    return false;
  }

  VBF_jjdEta = -9999.; //small enough initial value
  VBF_Mjj  = -9999.; //small enought initial value

  int Njet=nCleanJetNotFat;
  for(int ci = 0; ci < Njet; ci++ ){
    //--momentum of 1st jet
    float pt1 = CleanJet_pt[ci];
    if(pt1<30){//pt cut
      continue;
    }
    float eta1 = CleanJet_eta[ci];
    if (fabs(eta1) > 4.7){
      continue;
    }
    float phi1 = CleanJet_phi[ci];
    float mass1 = Jet_mass[CleanJetNotFat_jetIdx[ci]];//no mass for cleanjet. Take mass for orig. jet collection


    for(int cj = 0; cj < Njet; cj++){
      if(ci>=cj) continue; // no need to check the same particle pair or already checked one
      
      float pt2 = CleanJet_pt[cj];
      if(pt2 < 30) continue;
      float eta2 = CleanJet_eta[cj];
      if(fabs(eta2) > 4.7) continue;
      float phi2 = CleanJet_phi[cj];
      float mass2 = Jet_mass[CleanJetNotFat_jetIdx[cj]];


      //if each forward jet passes the cuts
      TLorentzVector v1,v2;
      v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1);
      v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2);


      float this_dEta = fabs(eta1-eta2);//dEta
      float this_Mjj  = (v1+v2).M();//Forward jets going to opposite direction

      if(this_Mjj < 500 ) continue;//Mjj cut
      if(this_dEta < 3.5 ) continue; // back to back
      if(this_dEta > VBF_jjdEta){// if current dEta is bigger than previous pair
	//take the current one
        VBF_jjdEta=this_dEta;
        VBF_Mjj=this_Mjj;
      }

    }
  }
  if(VBF_jjdEta < 3.5){//if not VBF event
    isVBFEvent=false;
    return false;
  }
  isVBFEvent=true;
  return true;

}

//To call VBF variables
float Get_VBF_jjdEta(int entry){  isVBFEvent=SetVBF(entry);
  if(!isVBFEvent){    return -9999;
  }
  else{    return VBF_jjdEta;
  }
}


float Get_VBF_Mjj(int entry){  isVBFEvent=SetVBF(entry);
  if(!isVBFEvent){    return -9999;
  }
  else{    return VBF_Mjj;
  }

}
