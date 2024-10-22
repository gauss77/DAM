package dam2.biblioteca.repositorio;

import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import dam2.biblioteca.modelo.Prestamo;

@Repository
public interface IPrestamoRepo extends CrudRepository<Prestamo, String>{
	
	@Modifying
	@Query("DELETE FROM Prestamo p WHERE p.usuario.dni = :dni")
	public void deletePrestamosFromUser(@Param("dni") String dni);
}
