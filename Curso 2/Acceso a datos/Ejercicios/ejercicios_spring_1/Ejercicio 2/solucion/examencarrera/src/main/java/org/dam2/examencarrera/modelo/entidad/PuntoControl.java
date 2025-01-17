package org.dam2.examencarrera.modelo.entidad;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.ManyToOne;


import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;


@Data
@NoArgsConstructor
@RequiredArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(onlyExplicitlyIncluded = true)
@Builder

@Entity

public class PuntoControl implements Serializable {

	@NonNull
	@EqualsAndHashCode.Include
	@Id
	private Float pk;
	private String juez;
	
	@ManyToOne (fetch = FetchType.EAGER,optional = true)
	private Corredor primero;
	
	private int tiempo;

}
