DICT_MjjShapeW={
    '2018':{
        'Boosted':{
            'w_min':1,
            'w_max':1
        },
        #w_min :    +0.666   -0.013/+0.014 (68%)
        #w_max :    +1.151   -0.009/+0.009 (68%)

        'Resolved':{
            'w_min':0.666,
            'w_max':1.151
        },

    },

    '2017':{

        'Boosted':{
            'w_min':1,
            'w_max':1
        },

        'Resolved':{
            'w_min':0.741,
            'w_max':1.073,
            'w_min_err':0.018,
            'w_max_err':0.011,

        },

        
    },
    
    '2016':{

        'Boosted':{
            'w_min':1,
            'w_max':1
        },

        'Resolved':{
            'w_min':0.848,
            'w_max':1.017,
            'w_min_err':0.016,
            'w_max_err':0.010,
        },

        
    },
    
}
for Year in DICT_MjjShapeW:
    for bst in DICT_MjjShapeW[Year]:
        w_min=DICT_MjjShapeW[Year][bst]['w_min']
        w_max=DICT_MjjShapeW[Year][bst]['w_max']
        
        DICT_MjjShapeW[Year][bst]['slope']=w_max-w_min
        DICT_MjjShapeW[Year][bst]['intercept']=w_min


        print DICT_MjjShapeW[Year][bst]['slope']
        print DICT_MjjShapeW[Year][bst]['intercept']
