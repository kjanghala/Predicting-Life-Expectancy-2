/*read csv file*/
proc import datafile= '/Data/Raw/health_ineq_online_table_5.csv'
	dbms=csv
	out = raw_data
	replace;
	getnames = yes;
run;

/*only keep columns that will be used*/
data raw_data; set raw_data;
	keep stateabbrv year le_agg_q1_F le_agg_q2_F le_agg_q3_F le_agg_q4_F le_agg_q1_M le_agg_q2_M le_agg_q3_M le_agg_q4_M;
	stateabbrv = lowcase(stateabbrv);
run;

/*separate by gender and re-combine*/
data female_data; set raw_data;
	gender = 'female';
	keep stateabbrv year gender le_agg_q1_F le_agg_q2_F le_agg_q3_F le_agg_q4_F;
	rename stateabbrv=state le_agg_q1_F=q1_le le_agg_q2_F=q2_le le_agg_q3_F=q3_le le_agg_q4_F=q4_le;
run;

data male_data; set raw_data;
	gender = 'male';
	keep stateabbrv year gender le_agg_q1_M le_agg_q2_M le_agg_q3_M le_agg_q4_M;
	rename stateabbrv=state le_agg_q1_M=q1_le le_agg_q2_M=q2_le le_agg_q3_M=q3_le le_agg_q4_M=q4_le;
run;

data cleaned_data; SET female_data male_data;
run;

/*separate by quartile and re-combine*/

data q1_data; set cleaned_data;
	quartile = 1;
	keep state year gender q1_le quartile;
	rename q1_le=LE;
run;

data q2_data; set cleaned_data;
	quartile = 2;
	keep state year gender q2_le quartile;
	rename q2_le=LE;
run;

data q3_data; set cleaned_data;
	quartile = 3;
	keep state year gender q3_le quartile;
	rename q3_le=LE;
run;

data q4_data; set cleaned_data;
	quartile = 4;
	keep state year gender q4_le quartile;
	rename q4_le=LE;
run;

data final_data; 
	retain state year quartile gender LE;
	set q1_data q2_data q3_data q4_data;
run;

/*export cleaned csv file*/
proc export data = final_data
	outfile='/Data/Derived/final_data.csv'
	dbms=csv
	replace;
run;

/*testing alternative model*/
data test_data; set final_data;
	if year = 2001 then new_year = 1;
	if year = 2002 then new_year = 2;
	if year = 2003 then new_year = 3;
	if year = 2004 then new_year = 4;
	if year = 2005 then new_year = 5;
	if year = 2006 then new_year = 6;
	if year = 2007 then new_year = 7;
	if year = 2008 then new_year = 8;
	if year = 2009 then new_year = 9;
	if year = 2010 then new_year = 10;
	if year = 2011 then new_year = 11;
	if year = 2012 then new_year = 12;
	if year = 2013 then new_year = 13;
	if year = 2014 then new_year = 14;
	drop year;
run;

data test_data; 
	retain state new_year quartile gender LE;
	set test_data;
run;

proc export data = test_data
	outfile='/Data/Derived/test_data.csv'
	dbms=csv
	replace;
run;

/*2018 income quartiles by state*/
proc import datafile= '/Data/Raw/state_by_percentile_2018.csv'
	dbms=csv
	out = reference
	replace;
	getnames = yes;
run;

data ref_2018;
	retain State _25th_Percentile Median _75th_Percentile;
	set reference;
	drop average _90th_Percentile Top_1_;
run;

proc export data = ref_2018
	outfile='/Data/Derived/ref_2018.csv'
	dbms=csv
	replace;
run;
