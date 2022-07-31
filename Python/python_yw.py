# @BEGIN PYTHON-DATA-CLEANING-PROCESS
# @PARAM filepath
# @IN Food_Inspections_OpenRefine_cleaned  @URI file:{filepath}\openrefine\Food_Inspections_OpenRefine_cleaned.xlsx
# @OUT Food_Inspections_Python_cleaned  @URI file:{filepath}\Food_Inspections_Python_cleaned.csv

    # @BEGIN TransformToPandasDF
    # @IN Food_Inspections_OpenRefine_cleaned
    # @OUT PANDAS_DATAFRAME
    # @END TransformToPandasDF

    # @BEGIN PHASE1-CLEANING
    # @IN PANDAS_DATAFRAME
    # @END PHASE1-CLEANING

    # @BEGIN PHASE1:FindMissingGPS
    # @IN PHASE1-CLEANING
    # @OUT MISSING_GPS_RECORDS
    # @END PHASE1:FindMissingGPS

    # @BEGIN PHASE1:FindMissingCity
    # @IN PHASE1-CLEANING
    # @OUT MISSING_CITY_RECORDS
    # @END PHASE1:FindMissingCity

    # @BEGIN PHASE1:FindMissingState
    # @IN PHASE1-CLEANING
    # @OUT MISSING_STATE_RECORDS
    # @END PHASE1:FindMissingCity


    # @BEGIN PHASE1:Iterate:Missing_GPS
    # @IN MISSING_GPS_RECORDS
    # @OUT getGPSByZipCode(Zip)
        # @BEGIN LocationByZipCode:Lat,Lng
        # @END LocationByZipCode:Lat,Lng
    # @END PHASE1:Iterate:Missing_GPS

    # @BEGIN PHASE1:Iterate:Missing_City
    # @IN MISSING_CITY_RECORDS
    # @OUT getCityByZipCode(Zip)
        # @BEGIN LocationByZipCode:CITY
        # @END LocationByZipCode:CITY
    # @END PHASE1:Iterate:Missing_City


    # @BEGIN PHASE1:Iterate:Missing_State
    # @IN MISSING_STATE_RECORDS
    # @OUT getStateByZipCode(Zip)
        # @BEGIN LocationByZipCode:State
        # @END LocationByZipCode:State
    # @END PHASE1:Iterate:Missing_State

    


    # @BEGIN getGPSByZipCode(Zip)
    # @PARAM Lat @AS Zip
    # @END getGPSByZipCode(Zip)

    # @BEGIN getCityByZipCode(Zip)
    # @PARAM Lat @AS Zip
    # @END getCityByZipCode(Zip)

    # @BEGIN getStateByZipCode(Zip)
    # @PARAM Lat @AS Zip
    # @END getStateByZipCode(Zip)

    

    #-------------------------------------

    # @BEGIN UpdatedGPS
    # @IN getGPSByZipCode(Zip)
    # @END UpdatedGPS
    
    # @BEGIN UpdatedCity
    # @IN getCityByZipCode(Zip)
    # @END UpdatedCity    

    # @BEGIN UpdatedState
    # @IN getStateByZipCode(Zip)
    # @END UpdatedState    
    

    # @BEGIN PHASE1:JoinResults
    # @IN UpdatedGPS
    # @IN UpdatedCity
    # @IN UpdatedState
    # @OUT COMBINED_DATASET
    # @END PHASE1:JoinResults  
    
    #-------------------------------------
    
    # @BEGIN PHASE2-CLEANING
    # @IN COMBINED_DATASET
    # @END PHASE2-CLEANING
    
    # @BEGIN PHASE2:FindNotNullViolation
    # @IN PHASE2-CLEANING
    # @OUT PHASE2:VIOLATION_RECORDS
    # @END PHASE2:FindNotNullViolation
    
    
    # @BEGIN PHASE2:Iterate:Violation_Iter
    # @IN PHASE2:VIOLATION_RECORDS
        # @END PHASE2:Iterate:Violation_Iter
        
        # @BEGIN PHASE2:CreateNewColumns
        # @PARAM Violation_Index
        # @IN PHASE2:Iterate:Violation_Iter
        # @OUT PHASE2:AddNewColumn
        # @END PHASE2:CreateNewColumns
        
    
    # @BEGIN PHASE2:Iterate:SplitViolation_Iter
    # @IN PHASE2:AddNewColumn
    # @OUT PHASE2:Splited_Violation_RECORDS
    # @END PHASE2:SplitViolation_Iter

    
    # @BEGIN PHASE2:Iterate:AddViolation_Iter
    # @PARAM Violation_Index
    # @IN PHASE2:Splited_Violation_RECORDS
    # @OUT PHASE2:UpdatedNewViolation
    # @END PHASE2:Iterate:AddViolation_Iter
    

    # @BEGIN RemoveOldViolationColumn
    # @IN PHASE2:UpdatedNewViolation
    # @OUT CLEAN_DATASET
    # @END RemoveOldViolationColumn
    
    

    # @BEGIN ConvertDataframeToCSV
    # @IN CLEAN_DATASET
    # @OUT Food_Inspections_Python_cleaned @URI file:{filepath}\Food_Inspections_Python_cleaned.csv
    # @END ConvertDataframeToCSV


# @END PYTHON-DATA-CLEANING-PROCESS


