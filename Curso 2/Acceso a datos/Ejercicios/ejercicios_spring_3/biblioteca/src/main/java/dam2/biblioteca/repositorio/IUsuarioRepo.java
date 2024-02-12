package dam2.biblioteca.repositorio;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import dam2.biblioteca.modelo.Usuario;

@Repository
public interface IUsuarioRepo extends CrudRepository<Usuario, String>{

}
