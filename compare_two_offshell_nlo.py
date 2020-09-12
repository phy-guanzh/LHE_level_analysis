import ROOT
import style
import CMS_lumi

ROOT.TH1.SetDefaultSumw2()
ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(ROOT.kTRUE)
style.GoodStyle().cd()

#samples=['wmwm_ll','wmwm_tl','wmwm_tt','wpwp_ll','wpwp_tl','wpwp_tt']
colorful=[ROOT.kRed,ROOT.kBlue,ROOT.kGreen,ROOT.kCyan]
#variables={'costheta11':'cos(#theta_{e})','costheta22':'cos(#theta_{#mu})','costheta1':'cos(#theta_{e})','costheta2':'cos(#theta_{#mu})','m_detajj':'#Delta#eta_{jj}','m_met':'p_{t}^{miss} [GeV]','m_mjj':'m_{jj} [GeV]','m_mll':'m_{ll} [GeV]','m_mlvlv':'m_{l#nul#nu} [GeV]','m_ptj1':'p_{t}^{j1} [GeV]','m_ptj2':'p_{t}^{j2} [GeV]','m_ptl1':'p_{t}^{e} [GeV]','m_ptl2':'p_{t}^{#mu} [GeV]'}
#variables={,'m_mlvlv':'m_{l#nul#nu} [GeV]'}
variables={
    #'zepp1':{'name':'Z^{*}_{l1}','rebin':1},
    #'zepp2':{'name':'Z^{*}_{l2}','rebin':1},
    'costheta1':{'name':'cos(#theta_{W_{1}})','rebin':1},
    'costheta2':{'name':'cos(#theta_{W_{2}})','rebin':1},
    'costheta11':{'name':'cos(#theta_{W_{1}})','rebin':1},
    'costheta22':{'name':'cos(#theta_{W_{2}})','rebin':1},
    'costheta13':{'name':'cos(#theta_{l1,W2})','rebin':1},
    'costheta23':{'name':'cos(#theta_{l2,W1})','rebin':1},
    #'m_detajj':{'name':'#Delta#eta_{jj}','rebin':1},
    #'m_dphijj':{'name':'#Delta#phi_{jj}','rebin':1},
    #'m_dphijj_2':{'name':'#Delta#phi_{jj}','rebin':1},
    #'m_dphill':{'name':'#Delta#phi_{ll}','rebin':1},
    'm_dphill_2':{'name':'#Delta#phi_{ll}','rebin':1},
    'm_met':{'name':'p_{T}^{miss} [GeV]','rebin':1},
    'm_met_2':{'name':'p_{T}^{miss} [GeV]','rebin':1},
    #'m_mjj':{'name':'m_{jj} [GeV]','rebin':1},
    #'m_mjj_2':{'name':'m_{jj} [GeV]','rebin':1},
    #'m_mjj_3':{'name':'m_{jj} [GeV]','rebin':1},
    'm_mll':{'name':'m_{ll} (GeV)','rebin':1},
    'm_mll_2':{'name':'m_{ll} (GeV)','rebin':1},
    'm_mll_3':{'name':'m_{ll} (GeV)','rebin':1},
    'm_mlvlv':{'name':'m_{l#nul#nu}','rebin':1},
    #'m_ptj1':{'name':'p_{T}^{j1} [GeV]','rebin':1},
    #'m_ptj1_2':{'name':'p_{T}^{j1} [GeV]','rebin':1},
    #'m_ptj2':{'name':'p_{T}^{j2} [GeV]','rebin':1},
    #'m_ptj2_2':{'name':'p_{T}^{j2} [GeV]','rebin':1},
    'm_ptl1':{'name':'p_{T}^{l1} [GeV]','rebin':1},
    'm_ptl2':{'name':'p_{T}^{l2} [GeV]','rebin':1},
    'm_ptl2_2':{'name':'p_{T}^{l2} [GeV]','rebin':1},
    #'etaj1':{'name':'#eta_{j1}','rebin':1},
    #'etaj2':{'name':'#eta_{j2}','rebin':1},
    'etal1':{'name':'#eta_{l1}','rebin':1},
    'etal2':{'name':'#eta_{l2}','rebin':1},
    'm_photon_pt':{'name':'p_{T}^{photon} [GeV]','rebin':1},
    'dR_lep_pho':{'name':'dR_{lep}^{pho} ','rebin':1},
    #'no_shape':{'name':'count','rebin':1},
}
#variables={'m_ptl1':'p_{t}^{e} [GeV]'}
#variables={'costheta11':'cos(#theta_{e})','costheta22':'cos(#theta_{#mu})','costheta1':'cos(#theta_{e})','costheta2':'cos(#theta_{#mu})','m_detajj':'#Delta#eta_{jj}','m_met':'p_{t}^{miss} [GeV]','m_mjj':'m_{jj} [GeV]','m_mll':'m_{ll} [GeV]','m_mlvlv':'m_{l#nul#nu} [GeV]','m_ptj1':'p_{t}^{j1} [GeV]','m_ptj2':'p_{t}^{j2} [GeV]','m_ptl1':'p_{t}^{e} [GeV]','m_ptl2':'p_{t}^{#mu} [GeV]'}
frame=''
subdir='wwa_scheme45'
#params = {
#    'polar272':{'name':'polar','samples':['VBS_SSWW_TT'+frame,'VBS_SSWW_TL'+frame,'VBS_SSWW_LL'+frame],'scale':[0.9722962041070317,0.9549387370405278,0.953620522749274]},
#}
params = {
    'polar272':{'name':'polar','samples':['wwa_final'+frame,'wwa_offshell'+frame],'scale':[0.9722962041070317,0.9549387370405278]},
}

xoffsetstart = 0.0
yoffsetstart = 0.0
xoffset = 0.35
yoffset = 0.06
#xpositions = [0.68,0.68,0.68,0.68,0.4,0.4,0.4,0.4,0.21,0.21,0.21,0.21]
#ypositions = [0,1,2,3,0,1,2,3,0,1,2,3]
xpositions = [0.50,0.50,0.50,0.47,0.47,0.47,0.47,0.21,0.21,0.21,0.21]
ypositions = [0,1,2,0,1,2,3,0,1,2,3]
def draw_legend(x1,y1,hist,label,options):

    legend = ROOT.TLegend(x1+xoffsetstart,y1+yoffsetstart,x1+xoffsetstart + xoffset,y1+yoffsetstart + yoffset)

    legend.SetBorderSize(     0)
    legend.SetFillColor (     0)
    legend.SetTextAlign (    12)
    legend.SetTextFont  (    42)
    legend.SetTextSize  ( 0.040)
    print(label)
    legend.AddEntry(hist,label,options)

    legend.Draw("same")

    #otherwise the legend goes out of scope and is deleted once the function finishes
    hist.label = legend

def createCanvasPads():
    c = ROOT.TCanvas("c", "canvas", 400, 400)
    # Upper histogram plot is pad1
    pad1 = ROOT.TPad("pad1", "pad1", 0.0, 0.34, 0.98, 0.98)
    pad1.SetBottomMargin(0.018)  # joins upper and lower plot
    #pad1.SetGridx()
    pad1.Draw()
    # Lower ratio plot is pad2
    c.cd()  # returns to main canvas before defining pad2
    pad2 = ROOT.TPad("pad2", "pad2", 0.0, 0.05, 0.98, 0.34)
    pad2.SetTopMargin(0)  # joins upper and lower plot
    pad2.SetBottomMargin(0.4)
    #pad2.SetGridx()
    pad2.Draw()

    return c, pad1, pad2

def createPlot(ivar,i,name,samples,scale):
    c1,pad1,pad2 = createCanvasPads()
    #    c1 = ROOT.TCanvas("c1", "c1",5,50,500,500)
    #c1.SetLogy()
    f2=ROOT.TFile.Open('wwa_scheme45.root')
    #h1=f2.Get(ivar+'_SSWW')
    #h1.Sumw2()
    #norm=h1.Integral()
    #h1.Rebin(variables[ivar]['rebin'])

    h2=f2.Get(ivar+'_wwa_offshell_lo'+frame)
    print(ivar+'_wwa_offshell_lo'+frame,h2.Integral())
    h2.Sumw2()
    h2.Scale(1/h2.Integral())
    #h2.Rebin(variables[ivar]['rebin'])
    h2.SetLineColor(colorful[1])
    h2.SetMarkerColor(colorful[1])
    h2.SetLineWidth(3)


    h3=f2.Get(ivar+'_wwa_offshell_nlo'+frame)
    h3.Sumw2()
    h3.Scale(1/h3.Integral())
    #h3.Rebin(variables[ivar]['rebin'])
    h3.SetLineColor(colorful[2])
    h3.SetMarkerColor(colorful[2])
    h3.SetLineWidth(3)
    
#    h4=f2.Get(ivar+'_VBS_SSWW_TT'+frame)
#    h4.Sumw2()
#    h4.Scale(1/h4.Integral())
    #h4.Rebin(variables[ivar]['rebin'])
#    h4.SetLineColor(colorful[2])
#    h4.SetMarkerColor(colorful[2])
#    h4.SetLineWidth(3)

    h2.SetMaximum(max(h2.GetMaximum(),h3.GetMaximum())*1.4)

    plot_name={'wwa_offshell_lo'+frame:'#bf{WWA scheme4(LO)}','wwa_offshell_nlo'+frame:'#bf{WWA scheme5(NLO)}'}
    legend_count=0

    h2.SetMinimum(0)
    h2.SetTitle("")
    h2.GetYaxis().SetTitle("A.U.")
    h2.GetYaxis().SetTitleSize(0.04)
    h2.GetYaxis().SetTitleFont(62)
    h2.GetXaxis().SetTitleSize(0.05)
    h2.GetXaxis().SetTitleFont(62)
    h2.GetXaxis().SetTitle(variables[ivar]['name'])
    pad1.cd()
    h2.Draw()
    draw_legend(xpositions[legend_count],0.84 - ypositions[legend_count]*yoffset,h2,plot_name['wwa_offshell_lo'+frame],"l")
    legend_count+=1

    draw_legend(xpositions[legend_count],0.84 - ypositions[legend_count]*yoffset,h3,plot_name['wwa_offshell_nlo'+frame],"l")
    h3.Draw("same e")
    
 #   legend_count+=1

#    draw_legend(xpositions[legend_count],0.84 - ypositions[legend_count]*yoffset,h4,plot_name['VBS_SSWW_TT'+frame],"l")
#    h4.Draw("same e")

    CMS_lumi.writeExtraText = 1
    CMS_lumi.extraText = "    Simulation"
    CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

    iPos = 0
    if( iPos==0 ): CMS_lumi.relPosX = 0.12
    iPeriod = 0
    CMS_lumi.CMS_lumi(c1, iPeriod, iPos)
     
    r_central = h2.Clone()
    r_central.Divide(h2)
    r_combine = h3.Clone()
    r_combine.Divide(h2) 
    r_combine.SetTitle('')
     
    
    r_central.SetMaximum(1.269)#1.451)#1.269)
    r_central.SetMinimum(0.749)
    r_central.SetTitle('')
    r_central.GetYaxis().CenterTitle(True)
    y = r_central.GetYaxis()
    y.SetNdivisions(505)
    y.SetTitle("Scheme 5 / 4")
    y.SetTitleSize(0.07)
    y.SetTitleFont(62)
    y.SetTitleOffset(0.6)
    y.SetLabelFont(43)
    y.SetLabelSize(11)
    x = r_central.GetXaxis()
    x.SetTitleSize(0.15)
    x.SetTitleFont(62)
    x.SetTitleOffset(1)
    x.SetLabelFont(43)
    x.SetLabelOffset(0.05)
    x.SetLabelSize(11)
    x.SetTitle(variables[ivar]['name'])
    pad2.cd()
    
    r_combine.SetMarkerStyle(0)
    r_combine.SetMarkerColor(1)
    r_central.SetFillColor(ROOT.kGray)
    r_central.SetFillStyle(3345)
    ROOT.gStyle.SetHatchesSpacing(0.3)
    ROOT.gStyle.SetHatchesLineWidth(1)
    r_central.SetMarkerSize(0)
    r_central.Draw('E2')

    l1=ROOT.TLine(x.GetXmin(),1.0,x.GetXmax(),1.0)
    l1.SetLineColor(ROOT.kRed)
    l1.SetLineStyle(1)
    l1.SetLineWidth(2)
    l1.Draw('SAME')
    r_combine.SetMarkerStyle(8)
    r_combine.SetMarkerSize(0.5)
    r_combine.SetLineWidth(2)
    r_combine.SetLineColor(ROOT.kBlack)
    r_combine.Draw('SAME X0E')
    fit1 = ROOT.TF1("kfactor","pol 1",x.GetXmin(),x.GetXmax())
    r_combine.Fit(fit1,"E");
 
    pad1.cd()
    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.07)
    kfact = fit1.GetParameter(0)
    latex.DrawText(0.5 ,0.70 , " kfactor = %.3f "%( kfact ))

    c1.RedrawAxis()
    c1.SaveAs(subdir+'/'+ivar+'_'+i+frame+'_shape.png')
    c1.SaveAs(subdir+'/'+ivar+'_'+i+frame+'_shape.pdf')
    c1.Close()
    f2.Close()
    
for ivar in variables:
    for i in params:
        createPlot(ivar,i,params[i]['name'],params[i]['samples'],params[i]['scale'])

'''
for isample in range(0,len(samples)):
    for ivar in variables:
        c1 = ROOT.TCanvas("c1", "c1",5,50,500,500)
        c1.SetLogy()
        tl = ROOT.TLegend(0.65,0.78,0.87,0.87)
        h1=f1.Get(ivar+'_'+samples[isample])
        h2=f2.Get(ivar+'_'+samples2[isample])
        #h1=f1.Get('m_ptl1_'+samples[isample])
        #h2=f2.Get('m_ptl2_'+samples2[isample])
        norm = h2.Integral()
        #h1.Scale(h2.Integral()/h1.Integral())
        #h1.Rebin(2)
        #h2.Rebin(2)
        if h1.GetMaximum() < h2.GetMaximum():
            h1.SetMaximum(h2.GetMaximum()*1.2)
        else:
            h1.SetMaximum(h1.GetMaximum()*1.2)
        h1.SetLineColor(ROOT.kRed)
        h1.SetMarkerColor(ROOT.kRed)
        h1.GetXaxis().SetTitle('p_{T} [GeV]')#variables[ivar]
        h1.SetTitle('VBS W^{-}W^{-}: pt')#+variables[ivar]
        h2.SetLineColor(ROOT.kBlue)
        h2.SetMarkerColor(ROOT.kBlue)
        h1.Draw("")
        h2.Draw("same E")

        tl.AddEntry(h1,'electron','l')
        tl.AddEntry(h2,'muon','l')
        tl.Draw('same')
        c1.SaveAs(ivar+'_'+samples[isample]+".pdf")
        c1.Close()
'''
