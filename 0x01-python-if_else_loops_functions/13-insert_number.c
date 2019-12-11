#include "lists.h"

/**
 * insert_node - inserts a node
 *
 * @head: the pointer to the head of the linked list
 * @number: the number to include in the n node field
 * Return: pointer to the new node else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;
	listint_t *tmp2;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	tmp = *head;
	if (!tmp || tmp->n >= number)
	{
		new->next = tmp, *head = new;
		return (new);
	}


	tmp2 = tmp->next;
	while (tmp && tmp2 && (tmp2->n < number))
		tmp = tmp->next, tmp2 = tmp->next;

	tmp->next = new, new->next = tmp2;
	return (new);
}
