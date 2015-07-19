# revision 30592
# category Package
# catalog-ctan /fonts/dozenal
# catalog-date 2013-05-20 17:36:30 +0200
# catalog-license lppl
# catalog-version 4.0
Name:		texlive-dozenal
Version:	4.0
Release:	9
Summary:	Typeset documents using base twelve numbering (also called "dozenal")
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/dozenal
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dozenal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dozenal.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dozenal.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports typesetting documents whose counters are
represented in base twelve, also called "dozenal". It includes
a macro by David Kastrup for converting positive whole numbers
to dozenal from decimal (base ten) representation. The package
also includes a few other macros and redefines all the standard
counters to produce dozenal output. Fonts, in Roman, italic,
slanted, and boldface versions, provide ten and eleven (the
Pitman characters preferred by the Dozenal Society of Great
Britain). The fonts were designed to blend well with the
Computer Modern fonts, and are available both as Metafont
source and in Adobe Type 1 format.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/dozenal/fdzb8a.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/fdzbi8a.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/fdzbs8a.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/fdzi8a.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/fdzr8a.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/fdzs8a.afm
%{_texmfdistdir}/fonts/map/dvips/dozenal/fdz.map
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars12.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars17.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars6.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars7.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars8.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars9.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchb10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx12.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx5.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx6.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx7.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx8.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx9.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbxi10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbxsl10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchit10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchit12.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchit7.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchit8.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchit9.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchsl10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchsl12.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchsl8.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchsl9.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozenal.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozenalb.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozenali.mf
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars12.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars17.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars6.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars7.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars8.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars9.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchb10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbxi10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchit10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchit12.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchit7.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchit8.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchit9.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzbc7t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzbc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzbi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzbi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzbo7t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzbo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzbo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzbs8a.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzr8r.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzrc7t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzro7t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzro8r.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzro8t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzs7t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzs8a.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzs8c.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzs8r.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzs8t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzsc7t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzsc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzso7t.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzso8c.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzso8r.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/fdzso8t.tfm
%{_texmfdistdir}/fonts/type1/public/dozenal/fdzb8a.pfb
%{_texmfdistdir}/fonts/type1/public/dozenal/fdzbi8a.pfb
%{_texmfdistdir}/fonts/type1/public/dozenal/fdzbs8a.pfb
%{_texmfdistdir}/fonts/type1/public/dozenal/fdzi8a.pfb
%{_texmfdistdir}/fonts/type1/public/dozenal/fdzr8a.pfb
%{_texmfdistdir}/fonts/type1/public/dozenal/fdzs8a.pfb
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzb7t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzb8c.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzb8t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzbc7t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzbc8t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzbi7t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzbi8c.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzbi8t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzbo7t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzbo8c.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzbo8t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzr7t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzr8c.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzr8t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzrc7t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzrc8t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzro7t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzro8c.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzro8t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzs7t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzs8c.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzs8t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzsc7t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzsc8t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzso7t.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzso8c.vf
%{_texmfdistdir}/fonts/vf/public/dozenal/fdzso8t.vf
%{_texmfdistdir}/tex/latex/dozenal/dozenal.sty
%doc %{_texmfdistdir}/doc/fonts/dozenal/README
%doc %{_texmfdistdir}/doc/fonts/dozenal/dozenal.pdf
%doc %{_texmfdistdir}/doc/fonts/dozenal/testdozchars.tex
%doc %{_texmfdistdir}/doc/fonts/dozenal/testfdzchars.tex
#- source
%doc %{_texmfdistdir}/source/fonts/dozenal/dozenal.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
