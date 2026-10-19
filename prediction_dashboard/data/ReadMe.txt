This folder contains integrated data from the National Air Pollution Surveillance (NAPS) Program. This folder should contain the following files:
	ReadMe.txt (this file):  Describes the data in the output files.
	data.csv:  Contains concentration data for the queried pollutants, stations and time period.
	pollutants.csv:  Contains additional information on the pollutants.
	analyses.csv:  Contains information on the analyses used to measure concentrations of the pollutants.
	samplers.csv:  Contains information on the samplers used to collect samples of the pollutants.
	stations.csv:  Contains additional information on the queried stations.
	query.csv:  Summarizes the query used to generate these files.
	
Note:  The symbol (*) indicates columns that can be used to associate data between tables.
Note:  For additional information on the NAPS Program, refer to the "NAPS Ambient Air Monitoring and Quality Assurance/Quality Control (QA/QC) Guidelines": https://ccme.ca/en/res/ambientairmonitoringandqa-qcguidelines_ensecure.pdf
Note:  To access additional data, including data from the NAPS continuous monitoring program, visit the NAPS Data Query Tool (https://environmental-maps.canada.ca/naps-snpa/) or the NAPS Data Portal (https://data-donnees.az.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/?lang=en).
Note:  Integrated data prior to 2019 are not yet available from the NAPS Data Query Tool. To access pre-2019 integrated data, use the NAPS Data Portal: https://data-donnees.az.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/?lang=en
Note:  Modifications to the integrated data published to the NAPS Data Query Tool are described at the end of this file.
Note:  For questions about the data, please contact rnspa-napsinfo@ec.gc.ca
Note:  Turning on word wrap in your text editor may make this file easier to read.

------------------------------
"data.csv" column descriptions
------------------------------
(*) Monitoring_Stream:  Monitoring stream that the data belongs to. Different monitoring streams use different samplers. Information on the sampler used for a specific NAPS ID, monitoring stream and time period is provided in the file "samplers.csv".
	PM2.5 RM:  Particulate matter ≤2.5 μm (fine) collected on Teflon filters using the NAPS reference method (RM)
	PM2.5-10:  Particulate matter ≤10 μm and ≥2.5 μm (coarse) collected on Teflon filters
	PM10:  Particulate matter ≤10 μm collected on Teflon filters
	PM2.5 Speciation:  Particulate matter ≤2.5 μm (fine) and volatile inorganic compounds collected using a combination of denuders and Teflon, nylon and quartz filters for speciation analysis
	Carbonyls:  Carbonyls
	PAC:  Polycyclic aromatic compounds
	VOC:  Volatile organic compounds
(*) Analysis:  Analysis used to measure the pollutant. Additional analysis information is provided in the file "analyses.csv".
(*) Parameter:  Pollutant or other parameter being measured. Additional pollutant information is provided in the file "pollutants.csv".
(*) NAPS_ID:  6-digit site identification. Additional site information is provided in the file "stations.csv". Note, the terms "site" and "station" are used interchangeably.
Sampling_Date_yyyy_mm_dd:  Date (yyyy-mm-dd) that the sample was collected. Note, software such as Microsoft Excel may display the date in a different format.
Sample_Type:  
	R:  Routine sample
	FB:  Field blank (sampling date is the date the blank sample was loaded into the sampler)
	TB:  Travel blank (sampling date is the date the blank sample was shipped to the sampling station)
Value:  Value of the pollutant concentration or other parameter. Zeros and negative values should be treated as values below the detection limit. A blank value denotes no data available.
Method_Detection_Limit:  The lowest value that the method can report with confidence.
Units:  Units of the pollutant concentration or other parameter. Data for a specific pollutant are always presented in the same units.
Validation_Code:  Code assigned to the data following final validation. All data have undergone preliminary validation and are fit for use, even if final validation has not been completed.
	V0:  Valid value
	V1:  Valid value - below detection limit
	V2:  Valid value - extreme or unusual value assessed and considered valid
	H1:  Historical data that have not been assessed or validated
	M1:  Missing value - no value available
	M2:  Missing value - invalidated
	[BLANK VALUE]:  Final validation has not been completed

Note:  Integrated PM2.5 sampling is conducted via two monitoring streams: speciation and reference method (RM). Speciation samples undergo more extensive analysis than RM samples.
Note:  Missing observations are represented as blank values (i.e. empty fields: ,,) in the Value column. Blank values do not indicate a concentration of zero.
Note:  Concentrations are calculated using actual volume at ambient conditions at the time of sampling.
Note:  Blank sample concentrations are calculated using the expected actual volume of the sampler. Routine sample concentrations are not blank corrected.
Note:  Method detection limits (MDLs) are reported with one significant figure. Concentrations are reported to the same number of decimal places as the MDL.
Note:  Final validation refers to level 3 validation, as described in the NAPS QA/QC Guidelines. Preliminary validation refers to level 0, 1 and 2 validations.
Note:  The first six columns (Monitoring_Stream, Analysis, Parameter, NAPS_ID, Sampling_Date_yyyy_mm_dd, Sample_Type) constitute a unique identifier for each piece of data.
Note:  If you prefer to work with the data in a pivoted format where each pollutant has its own column, the data are published this way on the ECCC Data Mart: https://data-donnees.az.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/?lang=en. You may also pivot the data yourself using software such as Microsoft Excel. In Excel, the following formula pivots the data so that each pollutant and its associated method detection limit are in their own column. To use this formula, copy it into the same sheet as the data.
       =PIVOTBY(D:F,A:C,G:H,LAMBDA(x,IF(COUNT(x)=1,SUM(x),"")),3,0,,0)

---------------------------------------------
"pollutants.csv" column descriptions
---------------------------------------------
(*) Analysis:  Analysis used to measure the pollutant concentration.
(*) Parameter:  Pollutant being measured.
Molecular_Formula:  Molecular formula of the pollutant.
Molar_Mass_g/mol:  Molar mass of the pollutant in grams per mole.
Number_Carbons:  Number of carbons per molecule of the pollutant.
Category:  Category of the pollutant (only available for VOC).
CAS_Number:  CAS registry number of the pollutant.
Units:  Units that concentrations of the pollutant are provided in.
Start_Year_Pollutant:  First year that the pollutant was measured by the specified analysis.
End_Year_Pollutant:  Last year that the pollutant was measured by the specified analysis. No value indicates that monitoring is ongoing as of the most recent data publication year.

Note:  Non-pollutant parameters such as ambient pressure, ambient temperature and PAH recoveries are not included in this file.
Note:  This file is currently static. It does not get filtered based on the query.
Note:  Start_Year_Pollutant and End_Year_Pollutant may differ by site. These columns indicate the first and last years that the pollutant was measured for any site.

-------------------------------------------
"analyses.csv" column descriptions
-------------------------------------------
(*) Monitoring_Stream:  Monitoring stream that the analysis belongs to.
(*) Analysis:  Analysis used to measure pollutant concentrations. Acronyms are defined below.
	PAH:  Polycyclic aromatic hydrocarbons
	OCEC:  Organic carbon & elemental carbon
	VOC C2-C3:  Short-chain (C2-C3) volatile organic compounds via gas chromatography with flame ionization detection
	VOC C3-C12:  Short-chain and long-chain (C3-C12) volatile organic compounds via gas chromatography with mass spectrometry detection
Observation_Type:
	FP:  PM2.5
	CP:  PM2.5-10
	XP:  PM10
	TP:  PM30 (total particulate)
	G:  Gas-phase (volatile)
Medium:  Medium that the sample is collected on. Acronyms are defined below.
	TF:  Teflon filter 
	NF:  Nylon filter
	QF:  Quartz filter
	CAD:  Citric acid-coated denuder
	SCD:  Na2CO3-coated denuder
	DNPH:  2,4-dinitrophenylhydrazine (DNPH)-coated silica gel cartridge
	TGFF:  Teflon bonded to glass fibre filter
	TGFF+PUF:  Teflon bonded to glass fibre filter + 2 polyurethane foam plugs
	CV:  Summa canister
Sample_Preparation:  Preparation of the sample prior to analysis.
Instrument:  Instrument used to perform the analysis.
Start_Date_Analysis:  First sampling date (yyyy-mm-dd) that the analysis was performed for the specified monitoring stream.
End_Date_Analysis:  Last sampling date (yyyy-mm-dd) that the analysis was performed for the specified monitoring stream. No value indicates that the analysis continues as of the most recent data publication year.

Note:  The sampler data analysis is not included in this file.
Note:  This file is currently static. It does not get filtered based on the query.
Note:  Analytes are sometimes added to or dropped from an analysis. To see when analytes have been added/dropped, refer to the Start_Year_Pollutant and End_Year_Pollutant columns in the file "pollutants.csv".
Note:  Concentrations of C3 compounds (propane and propylene) are measured by both the VOC C2-C3 and VOC C3-C12 analyses; however, typically only the C3 data from the VOC C3-C12 analysis are reported. C3 data from the VOC C2-C3 analysis are reported when these data are not available from the VOC C3-C12 analysis. 
Note:  The total elements analysis, acid-digested metals analysis (also known as near-total metals) and water-soluble metals analysis measure many of the same elements. Care should be taken to use data from the method that best suits the purpose of the study. Total elements data and acid-digested metals data are recommended to be used for air quality standards for toxic elements or for source apportionment studies. Water-soluble metals data are recommended to be used to evaluate toxic effects on humans and ecosystems.
Note:  PAC data are not recovery-corrected; however, recoveries of internal PAC surrogates are provided with PAC data so that users may recovery-correct PAC data themselves if desired. The use of recovery correction could lead to results closer to the real values by decreasing the negative bias due to losses that occur during the analytical process. Recovery correction is performed by dividing the reported PAC concentration by the recovery of its surrogate.
Note:  The volatile nitrate analysis measures semi-volatile nitrate (primarily ammonium nitrate) lost during sampling and captured by nylon filters. The particulate phase ions analysis measures nitrate retained in the PM2.5 particles collected on Teflon filters. Total nitrate concentrations in PM2.5 are obtained by summing both measurements. Total nitrite concentrations in PM2.5 are obtained analogously; however, nitrite measurements have been discontinued due to the concentrations usually being below the MDL.
Note:  For the OCEC analysis, A and B refer to the two different quartz filters used in the analysis. The abbreviations OC, EC and TC mean organic carbon, elemental carbon and total carbon, respectively. The calculation of OCEC values is summarized below. POC(B) is not reported; however it is typically zero.
       Corrected total carbon: TC(corr) = OC(corr) + EC(A)
       Corrected organic carbon: OC(corr) = OC(A) - OC(B)
       Total carbon filter A: TC(A) = OC(A) + EC(A)
       Organic carbon filter A: OC(A) = OC1(A) + OC2(A) + OC3(A) + OC4(A) + POC(A)
       Organic carbon filter B: OC(B) = OC1(B) + OC2(B) + OC3(B) + OC4(B) + POC(B)
       Elemental carbon filter A: EC(A) = EC1(A) + EC2(A) + EC3(A) - POC(A)

-------------------------------------------
"samplers.csv" column descriptions
-------------------------------------------
(*) NAPS_ID:  NAPS ID of the site that the sampler belongs to.
(*) Monitoring_Stream:  Monitoring stream that the sampler belongs to.
Start_Date_Sampler:  Approximate date (yyyy-mm-dd) that the sampler started operation. No value indicates that the sampler started operation before 2010.
End_Date_Sampler:  Approximate date (yyyy-mm-dd) after which the sampler stopped operation, paused for an extended period (> 1 year), or switched to a different sampling frequency. No value indicates that the sampler is operational as of the most recent data publication year.
Sampler_Description:  Manufacturer and model of the sampler.
Sampling_Frequency:  Frequency of sample collection.
Sampling_Interval:  Duration and time interval of sample collection.
Sampler_Notes:  Notes about changes and interruptions to the sampler. [YYYY] indicates which year the note applies to. 

Note:  This file is currently static. It does not get filtered based on the query.
Note:  The sampler start date may be earlier than the first instance of valid data from the sampler, and the sampler end date may be later than the last instance of valid data from the sampler.
Note:  In the case of power outages or other exceptional events, the sampling interval can vary slightly from what is stated here. When a large portion (typically > 1 hour) of the sampling interval is missed, the sample is considered invalid.

----------------------------------
"stations.csv" column descriptions
----------------------------------

Station information
-------------------
(*) NAPS_ID:  6-digit site identification. The first two digits identify the province or territory. Site IDs are assigned by Environment and Climate Change Canada (ECCC) in no particular order.
Station_Name:  Common name given to the site by the Province or Territory.
Status:	 Indicates whether the station was active (1) or inactive (0) in the current Station List year.
Location_Address:  Street address or location.
City:  Municipality or place name.
Province/Territory_EN:  Province or territory in English.
Province/Territory_FR:  Province or territory in French.
Postal_Code:  6-digit alphanumeric postal code.
Timezone_UTC:  Time zone relative to Coordinated Universal Time (UTC) that data from the station are reported in. Data are usually reported in local standard time; however, there are exceptions since some provinces or territories that span multiple time zones choose to use a single time zone for reporting data. UTC is the primary time standard by which the world regulates clocks and time.
Latitude:  Latitude is a geographic coordinate that specifies the north–south position of a point on the Earth's surface.
Longitude:  Longitude is a geographic coordinate that specifies the east–west position of a point on the Earth's surface.
Elevation_m:  Elevation of the monitoring station at ground level above sea level in metres.
Start_Date_Station_yyyy_mm_dd:  Date (yyyy-mm-dd) when monitoring began at the site. Note: some measurement parameters may have been added or removed after this date.
End_Date_Station_yyyy_mm_dd:  Date (yyyy-mm-dd) when monitoring ended at the site. Note: some measurement parameters may have been removed before this date. No value indicates that monitoring is ongoing as of the most recent data publication year.
Combined_Stations:  The site IDs associated with a station that has moved locations. Data from these sites may be combined for trend analysis. Site combinations are determined in collaboration with provinces and territories. Factors such as proximity, elevation, inlet height and station classification are considered when determining if two sites can be combined for trend analysis.
Inlet_Height_m:  Height of the inlet probe above ground level in metres. Unless stated otherwise, the inlet height applies to all pollutants measured at the station.
Network:  Site identified in the most recent version of a Provincial or Territorial Annex to the NAPS Memorandum of Understanding, indicated by "N". Ozone sites operated by ECCC's Canadian Air and Precipitation Monitoring Network (CAPMoN) are indicated by the "C".

Pollutants measured
An X indicates that monitoring of the pollutant at the station is ongoing. An H indicates that the station has historical data for the pollutant, but that monitoring is not ongoing.
-------------------
SO2:  Sulphur dioxide
CO:  Carbon monoxide
NO2:  Nitrogen dioxide
NO: Nitric oxide
NOX:  Nitrogen oxides (NO + NO2)
O3:  Ground-level ozone
PM2.5_Continuous:  Particulate matter less than 2.5 microns via continuous monitoring.
PM10_Continuous:  Particulate matter less than 10 microns via continuous monitoring.
PM2.5_RM:  Particulate matter less than 2.5 microns (NAPS reference (gravimetric) method) via integrated monitoring.
PM10_Integrated:  Particulate matter less than 10 microns via integrated monitoring.
PM2.5-10:  Coarse particulate matter less than 10 microns and greater than 2.5 microns via integrated monitoring. 
PM2.5_Speciation:  Fine particulate matter less than 2.5 microns (chemical constituents) and volatile inorganic compounds via integrated monitoring.
VOC:  Volatile organic compounds via integrated (canister) monitoring.
Carbonyl:  Aldehydes and ketones via integrated monitoring.
PAC:  Polycyclic aromatic compounds via integrated monitoring.

Station classification
----------------------
Site_Type:  Characterizes sites in terms of source influences.
	PE Site_Type:  General Population Exposure - site located in an urban area where populations live, work, shop, play, and that are not classified as transportation or point sources.
	RB Site_Type:  Regional Backgrounds - site outside urban area.
	T Site_Type:  Transportation source–influenced - site within 100 m of a major road or influenced by off-road vehicles and engines, rail, marine or aviation sources located in an urban area.
	PS Site_Type:  Point source–influenced - site located in a populated area, near (< ~10 km) a major stationary emissions source (>= 1 kt per year); classification based on VOC and SO2 ambient measurement data.
Urbanization:  The degree of urbanization around the monitoring site. Population centre (PC) classification (Statistics Canada 2017a, Dictionary) is used to define levels of urbanization.
	LU Urbanization:  Large Urban Area - large population centre (population ≥ 100,000)
	MU Urbanization:  Medium Urban Area - medium population centre (population between 30,000 and 99,999)
	SU Urbanization:  Small Urban Area - small population centre (population between 1,000 and 29,999)
	NU Urbanization:  Non-Urban (Rural) Area - non-urban area (population < 1,000)
Neighbourhood:  The size of residential populations residing within 4 km of NAPS monitoring sites. A distance of 4 km represents the maximum distance associated with a neighbourhood scale of spatial representativeness.
	P1 Neighbourhood:  Neighbourhood population < 500
	P2 Neighbourhood:  Neighbourhood population 500–9,999 
	P3 Neighbourhood:  Neighbourhood population 10,000–49,999
	P4 Neighbourhood:  Neighbourhood population 50,000–99,999
	P5 Neighbourhood:  Neighbourhood population 100,000–149,999
	P6 Neighbourhood:  Neighbourhood population ≥ 150,000
Land_Use:  Represents the dominant land use category within a 400 m radius around each site. A radius of 400 m represents the middle scale of spatial representativeness.
	R Land_Use:  Residential
	C Land_Use:  Commercial
	I Land_Use:  Industrial
	P Land_Use:  Parks
	W Land_Use:  Water
	A Land_Use:  Agriculture
	F Land_Use:  Forested
	O Land_Use:  Open
Scale:  The spatial scale of representativeness the air sample with the scale most appropriate for the monitoring objective at the site.
	MI Scale:  Micro - Concentrations in air typical of areas ranging from several metres up to approximately 100 m.
	M Scale:  Middle - Concentrations in air typical of areas up to several city blocks ranging from about 100 m to 0.5 km.
	N Scale:  Neighbourhood - Concentrations in air typical of some extended area of the city that has relatively uniform land use on the order of 0.5-4 km.
	U Scale:  Urban - Concentrations in air typical of the overall city-wide area on the order of 4-50 km.
	R Scale:  Regional - usually a non-urban area of reasonably homogenous geography that may extend from tens to hundreds of kilometers (U.S. EPA, 1997).
PC:  Population Centre
CD:  Census Division
CSD:  Census Subdivision
CMA/CA:  Census Metropolitan Area/Census Agglomeration
AQMS_Airzone:  Air Quality Management System - Provincial/Territorial Air Zone
Core_Site:  Core sites include a comprehensive set of measurements at a select number of representative locations across Canada that addresses multiple monitoring objectives. Tier (T)1 core sites are based on the PM2.5 speciation sampling sites. Tier (T)2 sites have NAPS PM2.5 reference method (gravimetric) samplers.

Note:  This file gets filtered to only show stations that have records in the file "data.csv". The full list of NAPS stations is available on the NAPS Data Portal: https://data-donnees.az.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/?lang=en

---------------------------
"stations.csv" data sources
---------------------------
Please refer to the NAPS QA/QC Guidelines for information on how classifications are determined: https://ccme.ca/en/res/ambientairmonitoringandqa-qcguidelines_ensecure.pdf
Each classification is derived from the following data sources

Census Division:  Census Division Boundaries (https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?Year=21)
Census Subdivision:  Census Subdivision Boundaries (https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?Year=21)
Census Metropolitan Area/Census Agglomeration:  Census Metropolitan Area/Census Agglomeration Boundaries (https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?Year=21)
Population Centre:  Population Centre Boundaries (https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?Year=21)
Urbanization:  Population Centre Boundaries (https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?Year=21)
Urbanization:  Population Centre Population Data (https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger.cfm?Lang=E)
Neighbourhood:  Dissemination Block Boundaries (https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?Year=21)
Neighbourhood:  Dissemination Block Population Data (https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger.cfm?Lang=E)
Land Use Land Cover:  Open Street Map Data (https://download.geofabrik.de/north-america/canada.html)
Land Use Land Cover:  Sentinel-2 10m (https://www.arcgis.com/apps/instant/media/index.html?appid=fc92d38533d440078f17678ebc20e8e2)
Site_Type:  NPRI Data (https://open.canada.ca/data/en/dataset/1fb7d8d4-7713-4ec6-b957-4a882a84fed3)
Site_Type:  NAPS QA/QC Data (https://ccme.ca/en/res/ambientairmonitoringandqa-qcguidelines_ensecure.pdf)
Scale:  NAPS QA/QC Data (https://ccme.ca/en/res/ambientairmonitoringandqa-qcguidelines_ensecure.pdf)

----------------------------
"query.csv" file description
----------------------------
Query Date:  Date (yyyy-mm-dd) that the data were downloaded from the NAPS Data Query Tool.
Date of Last Data Publication:  Date (yyyy-mm-dd) when integrated data were most recently updated in the NAPS Data Query Tool. Updates may include both publication of new data and corrections to existing data, if issues were discovered.
Database:  Indicates whether data were queried from the continuous or integrated database.
Pollutants:  Pollutants that data were queried for.
Province/Territory:  Provinces and territories that data were queried for.
City/Town:  Cities and towns that data were queried for.
Station:  Stations that data were queried for.
Time period:  Date range (yyyy-mm-dd) that data were queried for.
Number of Records:  Number of records returned by the query.

Note:  This file summarizes the query differently than the "Summary of query and results" section of the NAPS Data Query Tool. The "Summary of query and results" section displays the time period and locations exactly as they were entered using the filters. This file filters the time period and locations to display only what the query returned data records for. For example, if Manitoba and Nunavut were both selected in the province/territory filter, but data are only available for Manitoba, this file will display only Manitoba.

---------------------------------------
Modifications to the integrated dataset
---------------------------------------
This section describes modifications to the integrated data published to the NAPS Data Query Tool.
Modifications to the metadata for stations, pollutants, analyses and samplers are not described here.
For additional information about modifications, please contact rnspa-napsinfo@ec.gc.ca

September 2026
--------------
Data published for the first time:
	- PM2.5 RM mass concentration, ambient pressure and ambient temperature data for 2026 routine (R) samples up to 2026-06-30.
	- Carbonyls data for 2025. 
Modifications to previously published data:
	- PM2.5 RM mass concentration data from station 020401 for 2025.
	- PM2.5 RM, PM2.5-10 and PM10 mass concentration data for 2019-2024.
	- Ambient pressure and ambient temperature data for 2019-2025.
	- PM2.5-10 ions data from station 129003 for 2021.
	- PM2.5-10 ions data from station 090230 for 2023.
	- Carbonyls data for 2024 (update only affects validation codes). 

June 2026
---------
Data published for the first time:
	- PM2.5 RM mass concentration, ambient pressure and ambient temperature data for 2025 routine (R) samples.
	- VOC data for 2025.
Changes to the format of the dataset:
	- In the Parameter column of the "data.csv" file, changed the name of "Butyraldehyde/Iso-butyraldehyde" to "Butyraldehyde/Iso-Butyraldehyde", to align with the name used for this analyte in the files on the NAPS Data Portal.

March 2026
----------
Data published for the first time:
	- PM2.5 RM, PM2.5-10, PM10, PM2.5 speciation, carbonyls, PAC and VOC data for 2019-2024. 
