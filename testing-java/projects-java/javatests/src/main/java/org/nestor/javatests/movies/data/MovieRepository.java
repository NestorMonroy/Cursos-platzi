package org.nestor.javatests.movies.data;

import org.nestor.javatests.movies.model.Movie;

import java.util.Collection;

public interface MovieRepository {
    Movie findById(long id);
    Collection<Movie> findAll();
    void saveOrUpdate(Movie movie);
}
