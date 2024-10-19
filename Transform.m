for GC = ["GC_ON","GC_OFF"]
    for res1 = ["Res1ActiveDetect","Res1ActiveEmpty","Res1InactiveDetect","Res1InactiveEmpty"]
        for res2 = ["Res2ActiveDetect","Res2ActiveEmpty","Res2InactiveDetect","Res2InactiveEmpty"]
            for res3 = ["Res3ActiveDetect","Res3ActiveEmpty","Res3InactiveDetect","Res3InactiveEmpty"]
                load("./SimulationOriginal/"+GC+"/"+res1+"/"+res2+"/"+res3+"/Circuit"+GC+"_"+res1+"_"+res2+"_"+res3+".mat")
                wavelength = transmition.wavelength;
                save("./Simulation/"+GC+"/"+res1+"/"+res2+"/"+res3+"/Circuit"+GC+"_"+res1+"_"+res2+"_"+res3+".mat")
            end
        end
    end
end