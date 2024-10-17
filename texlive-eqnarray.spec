Name:		texlive-eqnarray
Version:	20641
Release:	2
Summary:	More generalised equation arrays with numbering
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eqnarray
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnarray.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnarray.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnarray.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
