Name:		texlive-eqnarray
Version:	1.3
Release:	1
Summary:	More generalised equation arrays with numbering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eqnarray
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnarray.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnarray.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnarray.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Defines an equationarray environment, that allows more than
three columns, but otherwise behaves like LaTeX's eqnarray
environment. This environment is similar, in some ways, to the
align environment of amsmath. The package requires the array
package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
