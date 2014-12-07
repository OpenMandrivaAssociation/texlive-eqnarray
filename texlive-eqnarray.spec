# revision 20641
# category Package
# catalog-ctan /macros/latex/contrib/eqnarray
# catalog-date 2010-12-02 11:00:56 +0100
# catalog-license gpl3
# catalog-version 1.3
Name:		texlive-eqnarray
Version:	1.3
Release:	9
Summary:	More generalised equation arrays with numbering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eqnarray
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnarray.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnarray.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnarray.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines an equationarray environment, that allows more than
three columns, but otherwise behaves like LaTeX's eqnarray
environment. This environment is similar, in some ways, to the
align environment of amsmath. The package requires the array
package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eqnarray/eqnarray.sty
%doc %{_texmfdistdir}/doc/latex/eqnarray/README
%doc %{_texmfdistdir}/doc/latex/eqnarray/eqnarray.pdf
#- source
%doc %{_texmfdistdir}/source/latex/eqnarray/eqnarray.drv
%doc %{_texmfdistdir}/source/latex/eqnarray/eqnarray.dtx
%doc %{_texmfdistdir}/source/latex/eqnarray/eqnarray.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 751539
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718358
- texlive-eqnarray
- texlive-eqnarray
- texlive-eqnarray
- texlive-eqnarray

