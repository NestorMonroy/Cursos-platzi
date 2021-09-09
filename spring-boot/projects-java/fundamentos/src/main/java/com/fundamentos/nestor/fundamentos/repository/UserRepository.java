package com.fundamentos.nestor.fundamentos.repository;

import com.fundamentos.nestor.fundamentos.entity.User;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    //Examples JPQL
    @Query("select u from User u where u.email=?1")
    Optional<User> findAllByUserEmail(String email);


    @Query("select u from User u where u.name like ?1%")
    List<User> findAndSort(String name, Sort sort);

    // Example Query method
    List<User> findByName(String name);
    Optional<User> findByEmailAndName(String email, String name);
}
