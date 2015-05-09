from classes.otclass import OttoProject
import numpy as np
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.grid_search import GridSearchCV

op = OttoProject("../data/")
op.load_original()
#range_n_estimators = [100,300, 900, 1500]
#range_max_features = [3, 10, 30]
range_max_depth = [5,10,20, 30]
params = [{"max_depth":range_max_depth}]
rf = RFC(n_estimators = 500)
clf = GridSearchCV(rf, params, n_jobs = -1, verbose = 2, scoring = 'log_loss')
clf.fit(op.subtrain_features, op.subtrain_classes)
print str(clf.best_score_)+"\n"
print str(clf.best_params_)+"\n"
print str(clf.grid_scores_)+"\n"
f=open("log_cv_rf.txt","w")
f.write(str(clf.grid_scores_))
f.close()