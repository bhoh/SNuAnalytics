#include <iostream>
#include <TTree.h>


namespace multidraw {

  extern thread_local TTree* currentTree;

}


float CleanFatJet_pt[10];
UInt_t nCleanFatJet;
void init(TTree* tree){
  tree->SetBranchAddress("CleanFatJet_pt", &CleanFatJet_pt);
  tree->SetBranchAddress("nCleanFatJet", &nCleanFatJet);

}






float PrintBranch(int entry){
  init(multidraw::currentTree);
  multidraw::currentTree->GetEntry(entry);
  

  float output=0;
  for(int i = 0; i < nCleanFatJet; i++){
    std::cout<<"i="<<i<<" x="<<CleanFatJet_pt[i]<<std::endl;
    output=i;
  }
  return output;
}
