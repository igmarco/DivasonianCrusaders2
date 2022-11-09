import numpy as np
import math as m

from MD.Casillas.Casilla import *
from MD.Casillas.Catapulta import *
from MD.Casillas.Colina import *
from MD.Casillas.Copa import *
from MD.Casillas.Curacion import *
from MD.Casillas.Normal import *

class Nodo():

    def __init__(self, casilla=None, fichaDefensora=None, fichaAtacante=None, cayoProyectil=False):
        self.casilla = casilla if casilla is not None else Normal()
        self.fichaDefensora=fichaDefensora
        self.fichaAtacante=fichaAtacante
        self.cayoProyectil=cayoProyectil

    def estaAqui(self,fichaOCasillaOFaccion):
        if fichaOCasillaOFaccion is None:
            return False
        elif fichaOCasillaOFaccion.equals(self.casilla) or fichaOCasillaOFaccion.equals(self.fichaDefensora) or \
                fichaOCasillaOFaccion.equals(self.fichaAtacante) or fichaOCasillaOFaccion==self.fichaDefensora.faccion \
                or fichaOCasillaOFaccion == self.fichaAtacante.faccion:
            return True

    def ponerFicha(self,ficha):
        if self.fichaDefensora is None:
            self.fichaDefensora = ficha
        else:
            self.fichaAtacante = ficha

    def quitarFicha(self,ficha):
        return None if ficha is None
        freturn = None
        if self.fichaDefensora.equals(ficha):
            freturn = self.fichaDefensora
            self.fichaDefensora = self.fichaAtacante
            self.fichaAtacante = None
        elif self.fichaAtacante.equals(ficha):
            freturn = self.fichaAtacante
            if self.fichaAtacante is not None:
                self.fichaDefensora.sufrirDano(self.fichaAtacante.realizarAtaque(self.fichaDefensora))
            self.fichaAtacante = None
        return freturn


    public void resolverTurno() {

    	//Resolvemos combate, damos curación y sufrimos hacha. ¿Algo más? Puede que resolver el disparo automático.
    	//Vale, no, resolver el disparo automático DESCARTADO.
    	//Claro, tenía que contemplar que hubiese hacha y que se la diese al último en pie (si lo hay).
    	//Epa, queda una cosa, saber si es una copa y resolver el daño también.
    	//Falta una última cosa. Si está el hacha divasónica tirada en el suelo, entonces la recoge la tropa.

    	this.resolverCombate();
    	this.darCuración();
    	this.sufrirHacha();

    	this.comprobarMuertes();

    	if(this.fichaAtacante != null) this.fichaAtacante.puedeMover = true;
    	if(this.fichaDefensora != null) this.fichaDefensora.puedeMover = true;

    	if(this.casilla.tieneHacha() && this.fichaDefensora != null && this.fichaAtacante == null) {

    		this.fichaDefensora.setHachaDivasónica(this.casilla.getHachaDivasónica());
    		this.casilla.setHachaDivasónica(null);

    	}

    	if(casilla.getHachaDivasónica() != null && fichaDefensora != null && fichaAtacante == null && fichaDefensora.getHachaDivasónica() == null) {

    		this.fichaDefensora.setHachaDivasónica(casilla.getHachaDivasónica());

    	}

    	if (this.casilla instanceof Copa && this.fichaDefensora != null && this.fichaAtacante == null && this.fichaDefensora.getFacción() != ((Copa) this.casilla).getFacción()) {

    		((Copa) this.casilla).sufrirDaño(this.fichaDefensora.realizarAtaque());

    	}

    }

	private void resolverCombate() {

		if(this.fichaDefensora != null && this.fichaAtacante != null) {

			this.fichaDefensora.sufrirDaño(this.fichaAtacante.realizarAtaque(this.fichaDefensora));
    		this.fichaAtacante.sufrirDaño(this.fichaDefensora.realizarAtaque(this.fichaAtacante));

		}

    }

    private void darCuración() {

    	if(this.casilla instanceof Curación) {

    		if(this.fichaDefensora != null) this.fichaDefensora.curarse(((Curación) this.casilla).curar());
    		if(this.fichaAtacante != null) this.fichaAtacante.curarse(((Curación) this.casilla).curar());

    	}

    }

    private void sufrirHacha() {

    	if(this.fichaDefensora != null) this.fichaDefensora.sufrirHacha();
    	if(this.fichaAtacante != null) this.fichaAtacante.sufrirHacha();

    }

    public void recibirDisparo(int daño) {

    	if(this.fichaDefensora != null)this.fichaDefensora.sufrirDaño(daño);
    	if(this.fichaAtacante != null)this.fichaAtacante.sufrirDaño(daño);

    	this.comprobarMuertes();

    }

    public boolean hayFicha() {

    	return (this.fichaDefensora != null);

    }

    public boolean hayDosFichas() {

    	return (this.fichaAtacante != null);

    }

    //DE HECHO, CREO QUE ESTE ES IGUAL QUE EL MÉTODO estáAquí(Facción f).
//    public boolean hayFicha(Facción fc) {
//
//    }

    //ESTO LO AGREGO PARA GESTIONAR LAS CARGAS Y LAS HUIDAS DESDE Tablero.
    public void ejecutarCrga() {

    	this.fichaDefensora.sufrirDaño(this.fichaAtacante.realizarCarga(this.fichaDefensora));

		if(this.casilla instanceof Colina) this.fichaAtacante.sufrirDaño((this.fichaDefensora.realizarAtaque(this.fichaAtacante)) + ((Colina) this.casilla).getDañoExtra());
		else this.fichaAtacante.sufrirDaño(this.fichaDefensora.realizarAtaque(this.fichaAtacante));

		this.comprobarMuertes();

    }

    public void ejecutarCrgasRespectivas() {

    	this.fichaDefensora.sufrirDaño(this.fichaAtacante.realizarAtaqueContraHuida(this.fichaDefensora));
    	this.fichaAtacante.sufrirDaño(this.fichaDefensora.realizarAtaqueContraHuida(this.fichaAtacante));

    	this.comprobarMuertes();

    }

    public void ejecutarAtaqueContraHuida(Ficha f) {
    	//OJO, f ES LA FICHA QUE HUYE!! NO LA QUE ATACA

    	if(f != null) {

    		if(f.equals(this.fichaDefensora)) this.fichaDefensora.sufrirDaño(this.fichaAtacante.realizarAtaqueContraHuida(this.fichaDefensora));
    		else if(f.equals(this.fichaAtacante)) this.fichaAtacante.sufrirDaño(this.fichaDefensora.realizarAtaqueContraHuida(this.fichaAtacante));

    		this.comprobarMuertes();

    	}

    }

    public void ejecutarAtaquesDeHuidas() {

    	if(this.hayDosFichas()) {

    		this.fichaDefensora.sufrirDaño(this.fichaAtacante.realizarCarga(this.fichaDefensora));
        	this.fichaAtacante.sufrirDaño(this.fichaDefensora.realizarCarga(this.fichaAtacante));

    	}

    	this.comprobarMuertes();

    }

    private void comprobarMuertes() {

    	if(this.fichaAtacante != null && this.fichaAtacante.estáMuerta()) {

    		if(fichaAtacante.tieneHacha() && fichaDefensora.getHachaDivasónica() == null) {

    			fichaDefensora.setHachaDivasónica(fichaAtacante.getHachaDivasónica());

    		}
    		this.fichaAtacante = null;

    	}
    	if(this.fichaDefensora != null && this.fichaDefensora.estáMuerta()) {

    		if(fichaDefensora.tieneHacha() && casilla.getHachaDivasónica() == null) {

    			casilla.setHachaDivasónica(fichaDefensora.getHachaDivasónica());

    		}

    		//ADVERTENCIA: POSIBLES PROBLEMAS DE PROG3
    		this.fichaDefensora = this.fichaAtacante;
    		this.fichaAtacante = null;

    	}

    }

    //POR SI SE HA TRABADO EN COMBATE ESTE TURNO.
    public void noPuedeMover(Ficha f) {

    	if (f != null) {

    		if(f.equals(this.fichaAtacante)) this.fichaAtacante.puedeMover = false;
        	else if(f.equals(this.fichaDefensora)) this.fichaDefensora.puedeMover = false;

    	}

    }

    public void noPuedenMover() {

    	if(this.fichaAtacante != null) this.fichaAtacante.puedeMover = false;
    	if(this.fichaDefensora != null) this.fichaDefensora.puedeMover = false;

    }

    public boolean puedeMover(Ficha f) {

    	if (f == null) return false;
    	if(f.equals(this.fichaAtacante)) return this.fichaAtacante.puedeMover;
    	else if(f.equals(this.fichaDefensora)) return this.fichaDefensora.puedeMover;
    	else return false;
    }